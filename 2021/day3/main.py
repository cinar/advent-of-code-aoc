#
# Advent of Code 2021 - Day 3
#
import re

#input_file = "sample.txt"
input_file = "input.txt"


#
# Part 1
#
def to_int(bits):
  return int("".join(map(str, bits)), 2)


count = 0
sums = None
with open(input_file, "r") as file:
  pattern = re.compile("[01]")
  for line in file.read().splitlines():
    bits = map(int, pattern.findall(line))
    count += 1
    sums = [s + b for (s, b) in zip(sums, bits)] if sums else bits

gamma = to_int([1 if s > (count / 2) else 0 for s in sums])
epsilon = pow(2, len(sums)) - 1 - gamma
power = gamma * epsilon

print(f"Power {power}")


#
# Part 2
#
def partition(condition, values):
  t = []
  f = []
  for v in values:
    if condition(v):
      t.append(v)
    else:
      f.append(v)
  return t, f


def filter_down(condition, all):
  for i in range(len(all[0])):
    if len(all) == 1:
      break
    ones, zeros = partition(lambda v: v[i] == 1, all)
    all = ones if condition(len(ones), len(zeros)) else zeros

  return all


with open(input_file, "r") as file:
  pattern = re.compile("[01]")
  numbers = [
    list(map(int, pattern.findall(line))) for line in file.read().splitlines()
  ]

oxygen = to_int(filter_down(lambda o, z: not (o < z), numbers)[0])
co2 = to_int(filter_down(lambda o, z: not (o >= z), numbers)[0])
rating = oxygen * co2

print(f"Rating {rating}")
