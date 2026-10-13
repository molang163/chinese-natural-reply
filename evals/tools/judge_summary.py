"""Turn GPT judge output into per-config average rank, average score, flags and head-to-head wins.

Usage: python judge_summary.py <it-number> [<it-number> ...] [--only cfg1,cfg2,...]
(reads judge/it<N>.raw.md and judge/it<N>.mapping.json; --only drops the other configs from every ranking first)
"""
import collections
import itertools
import json
import re
import statistics
import sys

ranks, scores, flags = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(collections.Counter)
wins = collections.Counter()
args = sys.argv[1:]
only = None
if "--only" in args:
    i = args.index("--only")
    only, args = set(args[i + 1].split(",")), args[:i] + args[i + 2:]
for it in args:
    raw = open(f"judge/it{it}.raw.md").read()
    m = re.search(r"```(?:json)?\s*(\[.*\])\s*```", raw, re.S)
    data = json.loads(m.group(1) if m else raw)
    mapping = json.load(open(f"judge/it{it}.mapping.json"))
    by_q = {int(k.split("-")[1]): v for k, v in mapping.items()}
    for q in data:
        lab2cfg = by_q[int(q["q"])]
        order = [lab2cfg[l] for l in q["ranking"] if only is None or lab2cfg[l] in only]
        for i, cfg in enumerate(order, 1):
            ranks[cfg].append(i)
        for lab, a in q["answers"].items():
            if only is not None and lab2cfg[lab] not in only:
                continue
            scores[lab2cfg[lab]].append(a["score"])
            flags[lab2cfg[lab]].update(a.get("flags") or [])
        for x, y in itertools.permutations(order, 2):
            if order.index(x) < order.index(y):
                wins[(x, y)] += 1
cfgs = sorted(ranks, key=lambda c: statistics.mean(ranks[c]))
print(f"{'config':12}{'n':>4}{'avg rank':>10}{'avg score':>11}  flags")
for c in cfgs:
    print(f"{c:12}{len(ranks[c]):>4}{statistics.mean(ranks[c]):>10.2f}{statistics.mean(scores[c]):>11.2f}  {dict(flags[c])}")
print("\nhead-to-head (row beats column, out of n questions):")
print(" " * 12 + "".join(f"{c[:10]:>12}" for c in cfgs))
for x in cfgs:
    print(f"{x:12}" + "".join(f"{(wins[(x, y)] if x != y else '-'):>12}" for y in cfgs))
