#
# Advent of Code 2022 - Day 7
#
from collections import defaultdict

#input_file = "sample.txt"
input_file = "input.txt"

#
# Part 1
#
tree = defaultdict(int)
with open(input_file, "r") as file:
  path = [""]
  for line in file.read().splitlines():
    parts = line.split()
    if parts[0] == "$":
      if parts[1] == "cd":
        if parts[2] == "/":
          path = [""]
        elif parts[2] == "..":
          path.pop()
        else:
          path.append(parts[2])
    elif parts[0] != "dir":
      size = int(parts[0])
      key = ""
      for p in path:
        key = f"{key}{p}/"
        tree[key] += size

print(sum(size for size in tree.values() if size <= 100000))

#
# Part 2
#
needed = 30000000 - (70000000 - tree["/"])
print(min([size for size in tree.values() if size >= needed]))
