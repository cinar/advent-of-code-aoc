#
# Advent of Code 2022 - Day 3 - Part 1
#
input_file = "part1.txt"

def priority(letter):
  priority = ord(common.pop())
  if priority >= 97:
    priority -= 96
  else:
    priority -= 38

  return priority

total = 0
for line in open(input_file, "r").read().splitlines():
  half = len(line) // 2
  a = set(line[:half])
  b = set(line[half:])

  common = a & b
  if common:
    total += priority(common.pop())

print(f"Total is {total}")
assert total == 7785

#
# Advent of Code 2022 - Day 3 - Part 2
#
input_file = "part2.txt"

total = 0

lines = open(input_file, "r").read().splitlines())
for i in range(0, len(lines), 3):
  a = set(lines[i])
  b = set(lines[i + 1])
  c = set(lines[i + 2])

  common = a & b & c
  if common:
    total += priority(common.pop())

print(f"Total is {total}")
assert total == 2633
