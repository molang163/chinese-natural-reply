#!/usr/bin/env python3
"""把中文自然回应的 5 条核心规则写进 Codex 的 AGENTS.md（默认是全局的 ~/.codex/AGENTS.md）。

这一段放在两行标记之间，AGENTS.md 里的其他内容不动。重复运行会把这一段换成最新的，不会写重复。

用法：
  python3 agents_md.py                  写入或更新
  python3 agents_md.py --remove         删掉这一段
  python3 agents_md.py --file PATH      改别的 AGENTS.md，比如某个项目里的
"""
import argparse
import os
import re

BEGIN = "<!-- chinese-natural-reply:begin -->"
END = "<!-- chinese-natural-reply:end -->"
BLOCK = """## 中文回复（chinese-natural-reply 核心规则）

用中文回复用户时，每一轮都照这几条，完整规则见 chinese-natural-reply 这个 skill：

- 第一句就回答用户这一轮问的；随口问的，几句话答完。
- 不说防御性的话：不划“能确认的是／还不能确定”的边界，不提没发生、没找到的事，不替用户纠正 ta 并没有的误解，不交代没做什么，估时间不套前提。
- 没把握、又会影响 ta 做决定的地方，整段对话只说一次，用一句平常的话。
- 说错了就一句“刚才说错了”，直接给对的；不解释刚才为什么那样说。
- 不打官腔，不套安慰模板。这些只管说话方式，该查的照样查。"""


def main():
    ap = argparse.ArgumentParser(description="把中文自然回应的核心规则写进 Codex 的 AGENTS.md")
    ap.add_argument("--file", help="要改的 AGENTS.md，默认是 $CODEX_HOME/AGENTS.md（通常是 ~/.codex/AGENTS.md）")
    ap.add_argument("--remove", action="store_true", help="删掉这一段")
    a = ap.parse_args()

    home = os.environ.get("CODEX_HOME") or os.path.join(os.path.expanduser("~"), ".codex")
    path = os.path.expanduser(a.file) if a.file else os.path.join(home, "AGENTS.md")
    old = ""
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            old = fh.read()

    wrapped = f"{BEGIN}\n{BLOCK}\n{END}"
    found = re.search(re.escape(BEGIN) + ".*?" + re.escape(END), old, re.S)
    if a.remove:
        if not found:
            print(f"{path} 里没有这一段。")
            return
        new = (old[:found.start()].rstrip("\n") + "\n\n" + old[found.end():].lstrip("\n")).strip("\n")
        new = new + "\n" if new else ""
        done = "已删掉"
    elif found:
        new = old[:found.start()] + wrapped + old[found.end():]
        done = "已更新"
    else:
        new = (old.rstrip("\n") + "\n\n" if old.strip() else "") + wrapped + "\n"
        done = "已写入"

    if new == old:
        print(f"{path} 里已经是最新的。")
        return
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new)
    print(f"{done}：{path}。新开的 Codex 对话生效。")


if __name__ == "__main__":
    main()
