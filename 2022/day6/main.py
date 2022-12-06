#
# Advent of Code 2022 - Day 6
#

#input_file="sample.txt"
input_file="input.txt"

#
# Part 1
#
def find_marker(length):
  with open(input_file, "r") as file:
    for line in file.read().splitlines():
      for i in range(length, len(line)):
        if len(set(line[i-length:i])) == length:
          print(f"Marker {i}")
          break

print("Part 1 markers are:")
find_marker(4)

#
# Part 2
#
print("Part 2 markers are:")
find_marker(14)
