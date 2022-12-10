""" AoC 2021 Day 8. """
from collections import defaultdict
from pathlib import Path

#INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"

#
# Part 1
#
count = 0
for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    _, outputs = (part.split(" ") for part in line.split(" | "))
    count += sum([1 for p in outputs if len(p) in [2, 4, 3, 7]])

print(count)

#
# Part 2
#
total = 0
for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    patterns, outputs = ([frozenset(p) for p in part.split(" ")]
                         for part in line.split(" | "))

    ltp = defaultdict(list)
    for pattern in patterns:
        ltp[len(pattern)].append(pattern)

    ptn = {}
    ptn[ltp[2][0]] = 1
    ptn[ltp[4][0]] = 4
    ptn[ltp[3][0]] = 7
    ptn[ltp[7][0]] = 8

    for p in ltp[5]:
        if not (ltp[2][0] - p):
            ptn[p] = 3
        elif not(ltp[4][0] - ltp[2][0] - p):
            ptn[p] = 5
        else:
            ptn[p] = 2

    for p in ltp[6]:
        if (ltp[2][0] - p):
            ptn[p] = 6
        elif not(ltp[4][0] - p):
            ptn[p] = 9
        else:
            ptn[p] = 0

    total += (int("".join([str(ptn[p]) for p in outputs])))

print(total)
