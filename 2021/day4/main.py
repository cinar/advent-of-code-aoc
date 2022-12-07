#
# Advent of Code 2021 - Day 4
#
import re

#input_file = "sample.txt"
input_file = "input.txt"

#
# Part 1 and 2
#
with open(input_file, "r") as file:
  pa = file.read().split("\n\n")
  na = [int(v) for v in pa[0].split(",")]
  ba = [[int(v) for v in re.findall("\d+", p)] for p in pa[1:]]

  ds = set()
  l = 5
  for n in na:
    ds.add(n)
    for b in ba:
      if n in b:
        r, c = divmod(b.index(n), l)
        rm = sum([1 if b[r * l + i] in ds else 0 for i in range(l)]) == l
        cm = sum([1 if b[i * l + c] in ds else 0 for i in range(l)]) == l
        if rm or cm:
          score = n * sum([v if v not in ds else 0 for v in b])
          print(f"Number {n} score {score}.")
          ba.remove(b)
