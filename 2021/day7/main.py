""" AoC 2021 Day 7 """
from pathlib import Path
from statistics import median

#INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"

#
# Part 1
#
pa = [int(p) for p in Path(INPUT_FILE).read_text(encoding="utf-8").split(",")]
m = int(median(pa))
f = sum([abs(p - m) for p in pa])
print(f"Fuel {f}")

#
# Part 2
#
f = min([sum(abs(p - n) * (abs(p - n) + 1) // 2 for p in pa)
        for n in range(min(pa), max(pa)+1)])
print(f"Fuel {f}")
