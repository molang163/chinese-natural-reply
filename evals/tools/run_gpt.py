"""Run the eval prompts through Codex (GPT) with a given version of the skill.

Each run gets a fresh git repo: the skill under test sits in <repo>/.agents/skills/chinese-natural-reply
(nothing for the "none" config), the user's global copy of the skill is hidden with a config override,
and GPT works inside <repo>/<project>. Paths carry no hint of which config is running.

Usage:
  python run_gpt.py --iteration 1 --config old=skill-snapshot --config none \
      [--evals 1,2,3] [--parallel 6] [--model gpt-6.1-sol] [--effort max]
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOBAL_SKILL = os.path.expanduser("~/.codex/skills/chinese-natural-reply/SKILL.md")
RUN_ROOT = os.environ.get("GPT_RUN_ROOT") or os.path.join(tempfile.gettempdir(), "cnr-gptruns")
SKILL_MARK = "chinese-natural-reply/SKILL.md"


def make_repo(fixture, skill_dir):
    root = os.path.join(RUN_ROOT, uuid.uuid4().hex[:10])
    project = os.path.join(root, fixture or "notes")
    os.makedirs(project)
    if fixture:
        shutil.copytree(os.path.join(WS, "fixtures", fixture), project, dirs_exist_ok=True)
    else:
        with open(os.path.join(project, "README.md"), "w") as fh:
            fh.write("# notes\n")
    # a config can combine sources with "+": skill folders go to .agents/skills, files become the repo's AGENTS.md
    for src in (skill_dir or "").split("+"):
        if src and os.path.isfile(src) and os.path.basename(src) == "prompt.md":
            # prompt-style projects (e.g. talk-normal) are installed as an always-on AGENTS.md block
            with open(os.path.join(root, "AGENTS.md"), "a") as fh:
                fh.write("# --- talk-normal BEGIN ---\n" + open(src).read().strip() + "\n# --- talk-normal END ---\n")
        elif src and os.path.isfile(src):
            with open(os.path.join(root, "AGENTS.md"), "a") as fh:
                fh.write(open(src).read())
        elif src:
            shutil.copytree(src, os.path.join(root, ".agents", "skills", skill_name(src)))
    git = ["git", "-c", "user.name=tester", "-c", "user.email=tester@localhost"]
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(git + ["add", "-A"], cwd=root, check=True)
    subprocess.run(git + ["commit", "-qm", "init"], cwd=root, check=True)
    return root, project


def skill_name(skill_dir):
    m = re.search(r"^name:\s*(\S+)", open(os.path.join(skill_dir, "SKILL.md")).read(), re.M)
    return m.group(1) if m else os.path.basename(skill_dir.rstrip("/"))


def parse_events(path):
    messages, commands, usage, skill_read = [], [], {}, False
    with open(path, errors="replace") as fh:
        for line in fh:
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") == "turn.completed":
                usage = ev.get("usage") or {}
            item = ev.get("item") or {}
            if ev.get("type") != "item.completed" or not item:
                continue
            if item.get("type") == "agent_message":
                messages.append(item.get("text") or "")
            else:
                blob = json.dumps(item, ensure_ascii=False)
                if SKILL_MARK in blob or re.search(r"\.agents/skills/[^/\s]+/SKILL\.md", blob):
                    skill_read = True
                if item.get("command"):
                    commands.append(item["command"])
    return messages, commands, usage, skill_read


def run_one(ev, config, skill_dir, iteration, model, effort, timeout):
    eval_dir = os.path.join(WS, f"iteration-{iteration}", f"eval-{ev['id']:02d}-{ev['name']}")
    run_dir = os.path.join(eval_dir, config)
    out_dir = os.path.join(run_dir, "outputs")
    if os.path.exists(os.path.join(out_dir, "reply.md")):
        return f"skip {ev['name']}/{config}"
    os.makedirs(out_dir, exist_ok=True)
    meta_path = os.path.join(eval_dir, "eval_metadata.json")
    if not os.path.exists(meta_path):
        with open(meta_path, "w") as fh:
            json.dump({"eval_id": ev["id"], "eval_name": ev["name"], "prompt": ev["prompt"], "assertions": []},
                      fh, ensure_ascii=False, indent=2)
    root, project = make_repo(ev.get("fixture"), skill_dir)
    cmd = [
        "codex", "exec", "-m", model, "-c", f'model_reasoning_effort="{effort}"', "-c", 'service_tier="default"',
        "-c", f'skills.config=[{{path="{GLOBAL_SKILL}", enabled=false}}]',
        "--ephemeral", "--json", "-s", "workspace-write", "-C", project,
        "-o", os.path.join(run_dir, "last_message.md"), ev["prompt"],
    ]
    # the local Codex bridge sometimes drops the connection (426 Upgrade Required); each run is a fresh
    # ephemeral session, so trying again is safe
    for attempt in range(3):
        t0 = time.time()
        with open(os.path.join(run_dir, "events.jsonl"), "w") as out, open(os.path.join(run_dir, "stderr.txt"), "w") as err:
            try:
                rc = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=out, stderr=err, timeout=timeout).returncode
            except subprocess.TimeoutExpired:
                rc = "timeout"
        if rc == 0 or "failed to connect" not in open(os.path.join(run_dir, "stderr.txt"), errors="replace").read():
            break
        time.sleep(10)
    dur = time.time() - t0
    messages, commands, usage, skill_read = parse_events(os.path.join(run_dir, "events.jsonl"))
    final = messages[-1] if messages else ""
    with open(os.path.join(out_dir, "reply.md"), "w") as fh:
        fh.write(final)
    with open(os.path.join(out_dir, "progress.md"), "w") as fh:
        fh.write("\n\n---\n\n".join(messages[:-1]))
    total = (usage.get("input_tokens") or 0) + (usage.get("output_tokens") or 0)
    with open(os.path.join(run_dir, "timing.json"), "w") as fh:
        json.dump({"total_tokens": total, "duration_ms": int(dur * 1000), "total_duration_seconds": round(dur, 1)}, fh)
    with open(os.path.join(run_dir, "run_meta.json"), "w") as fh:
        json.dump({"config": config, "model": model, "effort": effort, "exit": rc, "skill_read": skill_read,
                   "usage": usage, "commands": commands, "repo": root}, fh, ensure_ascii=False, indent=2)
    return f"done {ev['name']}/{config} rc={rc} {dur:.0f}s skill_read={skill_read} chars={len(final)}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iteration", type=int, required=True)
    ap.add_argument("--config", action="append", required=True, help="name or name=skill_dir (relative to workspace)")
    ap.add_argument("--evals", default="")
    ap.add_argument("--evals-file", default="evals.json")
    ap.add_argument("--parallel", type=int, default=6)
    ap.add_argument("--model", default="gpt-6.1-sol")
    ap.add_argument("--effort", default="max")
    ap.add_argument("--timeout", type=int, default=1800)
    args = ap.parse_args()
    evals = json.load(open(os.path.join(WS, "evals", args.evals_file)))["evals"]
    if args.evals:
        keep = {int(x) for x in args.evals.split(",")}
        evals = [e for e in evals if e["id"] in keep]
    configs = []
    for c in args.config:
        name, _, sk = c.partition("=")
        srcs = [s if os.path.isabs(s) else os.path.join(WS, s) for s in sk.split("+")] if sk else []
        configs.append((name, "+".join(srcs) or None))
    jobs = [(e, n, s) for e in evals for (n, s) in configs]
    print(f"{len(jobs)} runs, parallel={args.parallel}, model={args.model}/{args.effort}", flush=True)
    with cf.ThreadPoolExecutor(args.parallel) as pool:
        futs = [pool.submit(run_one, e, n, s, args.iteration, args.model, args.effort, args.timeout) for e, n, s in jobs]
        for f in cf.as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as exc:  # keep the batch going
                print("error:", repr(exc), flush=True)


if __name__ == "__main__":
    sys.exit(main())
