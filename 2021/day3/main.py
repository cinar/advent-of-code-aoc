#
# Advent of Code 2021 - Day 3
#
input_file = "sample.txt"
#input_file = "input.txt"

#
# Part 1
#
lenghth = 6
sums = [0] * lenghth
count = 0
with open(input_file, "r") as file:
  for line in file.read().splitlines():
    count += 1
    for i in range(lenghth):
      sums[i] += int(line[i])

print(sums)
