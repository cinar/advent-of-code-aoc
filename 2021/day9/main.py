""" AoC 2021 Day 9. """
from pathlib import Path
import pprint

INPUT_FILE = "sample.txt"
#INPUT_FILE = "input.txt"

area = []
for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    area.append([int(c) for c in line])

#
# Part 1
#
count = 0
for i, row in enumerate(area):
    for j, value in enumerate(row):
        if all([
            ((j == 0) or (area[i][j - 1] > value)),
            ((i == 0) or (area[i-1][j] > value)),
            ((j == (len(row) - 1)) or (area[i][j + 1] > value)),
            ((i == (len(area) - 1)) or (area[i+1][j] > value))
        ]):
            count += (1 + value)

print(count)

