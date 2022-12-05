#
# Advent of Code 2021 - Day 1
#

#input_file = "sample.txt"
input_file = "input.txt"

#
# Part 1
#
with open(input_file, "r") as file:
  depths = list(map(int, file.read().splitlines()))
  count = sum(
    [1 if depths[i - 1] < depths[i] else 0 for i in range(1, len(depths))])
  print(f"Larger count is {count}.")

#
# Part 2
#
with open(input_file, "r") as file:
  depths = list(map(int, file.read().splitlines()))
  sums = [sum(depths[i:i + 3]) for i in range(0, len(depths) - 2)]
  count = sum([1 if sums[i - 1] < sums[i] else 0 for i in range(1, len(sums))])
  print(f"Larger count is {count}.")
