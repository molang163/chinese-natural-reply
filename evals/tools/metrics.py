"""Rough pattern counts per config for one iteration (diagnostic only, not a pass/fail score)."""
import json, os, re, sys, statistics
FAM = {
    "防御/边界": r"不能确定|还不能|不能据此|不足以|不代表|没有证据|尚未(证实|确认|验证|复验|核实)|仅凭|不能保证|没法保证|无法(保证|确认|判断|完整)|未必|能确认的是|很容易猜错|把握(很低|不大)|没什么把握",
    "没改什么": r"没有(修改|改动|删除|动)|未(删除|修改|改动)|均未|保持不变|未改动",
    "验证细节": r"\d+ ?项.{0,6}(通过|检查)|校验|读回|回归测试",
    "加粗": r"\*\*[^*\n]+\*\*",
    "网页链接": r"\]\(https?://",
    "表格": r"^\s*\|.*\|\s*$",
    "公文词": r"因此|据此|即可|现已|本次|本轮|核验|复验|落实|闭环|收口|兜底",
    "冒号揭晓": r"(的是|就是|在于|原因是|结论是|区别是)：",
    "宣布skill": r"chinese-natural-reply|中文自然回应|中文自然回复|技能",
}
it = sys.argv[1]; configs = sys.argv[2:]
rows = {c: [] for c in configs}
for name in sorted(os.listdir(it)):
    for c in configs:
        p = os.path.join(it, name, c, "outputs")
        if os.path.exists(os.path.join(p, "reply.md")):
            rows[c].append((open(os.path.join(p, "reply.md")).read(), open(os.path.join(p, "progress.md")).read()))
print("指标".ljust(14), *[f"{c:>10}" for c in configs])
print("回复数".ljust(14), *[f"{len(rows[c]):>10}" for c in configs])
print("字数中位数".ljust(14), *[f"{statistics.median(len(r) for r, _ in rows[c]):>10.0f}" for c in configs])
for k, rx in FAM.items():
    rx = re.compile(rx, re.M)
    if k == "宣布skill":
        vals = [sum(1 for _, p in rows[c] if rx.search(p)) for c in configs]
        print("进度里宣布skill".ljust(12), *[f"{v:>10}" for v in vals]); continue
    vals = [sum(1 for r, _ in rows[c] if rx.search(r)) for c in configs]
    print(k.ljust(14), *[f"{v:>10}" for v in vals])
