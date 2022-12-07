#
# Advent of Code 2021 - Day 5
#
import re

#input_file = "sample.txt"
input_file = "input.txt"

#
# Part 1
#
overlap = set()
with open(input_file, "r") as file:
  diagram = set()
  for line in file.read().splitlines():
    x1, y1, x2, y2 = map(int, re.findall("\d+", line))
    points = None
    if x1 == x2:
      points = set([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)])
    elif y1 == y2:
      points = set([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)])
    else:
      continue
    overlap |= diagram & points
    diagram |= points

count = len(overlap)
print(f"Count {count}")


#
# Part 2
#
def range2(s, e):
  if e >= s:
    return range(s, e + 1)
  else:
    return range(s, e - 1, -1)


overlap = set()
with open(input_file, "r") as file:
  diagram = set()
  for line in file.read().splitlines():
    x1, y1, x2, y2 = map(int, re.findall("\d+", line))
    points = None
    if x1 == x2:
      points = set([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)])
    elif y1 == y2:
      points = set([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)])
    else:
      points = set([(x, y) for x, y in zip(range2(x1, x2), range2(y1, y2))])
    overlap |= diagram & points
    diagram |= points

count = len(overlap)
print(f"Count {count}")
