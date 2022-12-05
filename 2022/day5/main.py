#
# Advent of Code 2022 - Day 5
#
import re

#input_file = "sample.txt"
input_file = "input.txt"

#
# Part 1
#
stacks = []
with open(input_file, "r") as file:
  for line in file.read().splitlines():
    if line.startswith("move"):
      c, f, t = map(int, re.sub("[^0-9 ]", "", line).split())
      for i in range(c):
        stacks[t - 1].insert(0, stacks[f - 1].pop(0))
    elif line.startswith(" 1"):
      pass
    else:
      for i in range(1, len(line), 4):
        stack_index = i // 4
        while len(stacks) <= stack_index:
          stacks.append([])
        if line[i] != " ":
          stacks[stack_index].append(line[i])

print("".join([stack[0] if stack else " " for stack in stacks]))

#
# Part 2
#
stacks = []
with open(input_file, "r") as file:
  for line in file.read().splitlines():
    if line.startswith("move"):
      c, f, t = map(int, re.sub("[^0-9 ]", "", line).split())
      for i in range(c):
        stacks[t - 1].insert(0, stacks[f - 1].pop(c - i - 1))
    elif line.startswith(" 1"):
      pass
    else:
      for i in range(1, len(line), 4):
        stack_index = i // 4
        while len(stacks) <= stack_index:
          stacks.append([])
        if line[i] != " ":
          stacks[stack_index].append(line[i])

print("".join([stack[0] if stack else " " for stack in stacks]))
