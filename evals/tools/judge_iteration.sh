#!/usr/bin/env bash
# Blind-judge one iteration with GPT: shuffled, unnamed answers + the rubric, scores and a ranking per question.
# Usage: CODEX_HOME=<home without AGENTS.md> judge_iteration.sh <iteration-number> <seed> cfg1 cfg2 ...
set -e
it=$1; seed=$2; shift 2
W=$(cd "$(dirname "$0")/.." && pwd)
n=$#; last=$(printf "ABCDEFGH" | cut -c$n)
cd "$W"
python3 tools/judge_bundle.py iteration-$it judge/it$it.bundle.md judge/it$it.mapping.json "$seed" "$@"
J=$(mktemp -d "${GPT_RUN_ROOT:-/tmp}/judge-it$it-XXXX")
cp evals/rubric.md "$J/评分标准.md"; cp judge/it$it.bundle.md "$J/答卷.md"
cd "$J" && git init -q
codex exec -m gpt-6.1-sol -c 'model_reasoning_effort="max"' -c 'service_tier="default"' --ephemeral -s read-only -C "$J" -o "$W/judge/it$it.raw.md" "你是评委。先读 评分标准.md，再读 答卷.md。答卷里有 16 道题，每道题有 $n 个回答（A–$last），它们来自同一个模型在不同设置下的输出，顺序已打乱。

请严格按评分标准给每个回答打 1–5 分，列出命中的扣分项（D/G/L/C/H，可以多个或没有），并为每个扣分项引用一小段原话作证据。最后把每道题的 $n 个回答从好到差排序。

不要猜测哪个回答来自哪种设置，只看文字本身。只输出一个 JSON 代码块，格式：
[{\"q\": 题号, \"answers\": {\"A\": {\"score\": 分数, \"flags\": [\"D\", ...], \"evidence\": \"原话摘录\"}, ...}, \"ranking\": [\"C\", \"A\", ...]}, ...]" < /dev/null > "$W/judge/it$it.log" 2>&1
echo "judge it$it exit $?"
