""" AoC 2022 Day 8 """
from itertools import takewhile
from pathlib import Path

# INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"

grid = Path(INPUT_FILE).read_text(encoding="utf-8").splitlines()

#
# Part 1
#
count = 0
for r, row in enumerate(grid):
    for c, tree in enumerate(row):
        count += (
            all(grid[r][i] < tree for i in range(c)) or
            all(grid[r][i] < tree for i in range(c + 1, len(row))) or
            all(grid[i][c] < tree for i in range(r)) or
            all(grid[i][c] < tree for i in range(r + 1, len(grid)))
        )

print(count)

#
# Part 2
#

def count_until(predicate, values):
    """ Count until predicate true. """
    n = 0
    for i in values:
        n += 1
        if predicate(i):
            break
    return n


dist = []
for r, row in enumerate(grid):
    for c, tree in enumerate(row):
        dist.append(
            count_until(lambda i: grid[i][c] >= tree, range(r - 1, -1, -1)) *
            count_until(lambda i: grid[r][i] >= tree, range(c - 1, -1, -1)) *
            count_until(lambda i: grid[i][c] >= tree, range(r + 1, len(grid))) *
            count_until(lambda i: grid[r][i] >= tree, range(c + 1, len(row)))
        )

print(max(dist))
