#
# Advent of Code 2022 - Day 4
#
import re

input_file = "input2.txt"

#
# Part 1
#
overlap = 0
with open(input_file, "r") as file:
  for line in file.read().splitlines():
    ab, ae, bb, be = map(int, re.split(r",|-", line))
    a = set(range(ab, ae + 1))
    b = set(range(bb, be + 1))
    if a.issubset(b) or b.issubset(a):
      overlap += 1

print(f"Overlap {overlap}")
assert overlap, 536

#
# Part 2
#
overlap = 0
with open(input_file, "r") as file:
  for line in file.read().splitlines():
    ab, ae, bb, be = map(int, re.split(r",|-", line))
    a = set(range(ab, ae + 1))
    b = set(range(bb, be + 1))
    if a & b:
      overlap += 1

print(f"Overlap {overlap}")
assert overlap, 845

