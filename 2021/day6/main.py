#
# Advent of Code 2021 - Day 6
#
from collections import Counter

#input_file = "sample.txt"
input_file = "input.txt"

#
# Part 1
#
with open(input_file, "r") as file:
  fa = list(map(int, file.read().split(",")))
  for i in range(80):
    count = len(fa)
    for i in range(count):
      if fa[i] == 0:
        fa[i] = 6
        fa.append(8)
      else:
        fa[i] -= 1

  print(len(fa))

#
# Part 2
#
with open(input_file, "r") as file:
  fa = Counter(list(map(int, file.read().split(","))))
  for i in range(256):
    fa = Counter({(k - 1): v for k, v in fa.items()})
    fa[6] += fa[-1]
    fa[8] = fa[-1]
    del fa[-1]

  print(sum(fa.values()))
