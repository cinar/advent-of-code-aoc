#
# Advent of Code 2022 - Day 1 - Part 1 and 2
#
input_file = "input2.txt"

# Each elf
elves = open(input_file, "r").read().split("\n\n")

# Total calories per elf
calories = list(map(lambda a: sum(map(int, a.split("\n"))), elves))

# Sorted by total calories
calories.sort(reverse=True)

# Part 1: Top calories
print(f"Elf with the most calories has {calories[0]} total calories.")
assert calories[0] == 69310

# Part 2: Top others
all = calories[0] + calories[1] + calories[2]
print(f"Top 3 elves with the most calories have {all} total calories.")
assert all == 206104
