"""Write an anonymized answer bundle for judging.

Per question, the answers from the given configs are shuffled and labelled A, B, C...; the bundle
shows only the prompt and the answers. The label -> config mapping is written to a separate file.

Usage: python judge_bundle.py <iteration-dir> <bundle.md> <mapping.json> <seed> cfg1 cfg2 ...
"""
import json
import os
import random
import sys

CONTEXT = {
    "todo": "（GPT 拿到一个记待办的 Python 小脚本，删除功能有 bug，可以直接改代码）",
    "study-site": "（GPT 拿到一个虚构的小项目：STATUS.md、TASKS.md 和一个只能记学习记录的小网站；STATUS.md 写的大部分功能代码不在项目里）",
}


def main():
    it_dir, bundle_path, map_path, seed, *configs = sys.argv[1:]
    ev_dir = os.path.join(os.path.dirname(it_dir.rstrip("/")), "evals")
    evals = {e["id"]: e for f in ("evals.json", "heldout.json") if os.path.exists(os.path.join(ev_dir, f))
             for e in json.load(open(os.path.join(ev_dir, f)))["evals"]}
    rng = random.Random(seed)
    out, mapping = [], {}
    for name in sorted(os.listdir(it_dir)):
        d = os.path.join(it_dir, name)
        if not (name.startswith("eval-") and os.path.isdir(d)):
            continue
        meta = json.load(open(os.path.join(d, "eval_metadata.json")))
        ev = evals[meta["eval_id"]]
        order = [c for c in configs if os.path.exists(os.path.join(d, c, "outputs", "reply.md"))]
        if len(order) != len(configs):
            print("missing answers in", name, file=sys.stderr)
        rng.shuffle(order)
        out.append(f"## 第 {meta['eval_id']} 题\n\n用户说：{meta['prompt']}\n")
        if ev.get("fixture"):
            out.append(CONTEXT.get(ev["fixture"], "") + "\n")
        mapping[name] = {}
        for label, cfg in zip("ABCDEFGH", order):
            reply = open(os.path.join(d, cfg, "outputs", "reply.md")).read().strip()
            out.append(f"### 回答 {label}\n\n{reply}\n")
            mapping[name][label] = cfg
        out.append("\n---\n")
    with open(bundle_path, "w") as fh:
        fh.write("\n".join(out))
    with open(map_path, "w") as fh:
        json.dump(mapping, fh, ensure_ascii=False, indent=1)
    print(len(mapping), "questions ->", bundle_path)


if __name__ == "__main__":
    main()
