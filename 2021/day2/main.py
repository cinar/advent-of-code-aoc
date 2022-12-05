#
# Advent of Code 2021 - Day 2
#
#input_file = "sample.txt"
input_file = "input.txt"

#
# Part 1
#
horizontal = 0
vertical = 0

with open(input_file, "r") as file:
  for line in file.read().splitlines():
    command, value = line.split()
    if command == "forward":
      horizontal += int(value)
    elif command == "down":
      vertical += int(value)
    elif command == "up":
      vertical -= int(value)

print(f"Horizontal {horizontal} vertical {vertical}")
multiple = horizontal * vertical
print(f"Multiple {multiple}")

#
# Part 2
#
horizontal = 0
vertical = 0
aim = 0

with open(input_file, "r") as file:
  for line in file.read().splitlines():
    command, value = line.split()
    if command == "forward":
      horizontal += int(value)
      vertical += int(value) * aim
    elif command == "down":
      aim += int(value)
    elif command == "up":
      aim -= int(value)

print(f"Horizontal {horizontal} vertical {vertical}")
multiple = horizontal * vertical
print(f"Multiple {multiple}")
