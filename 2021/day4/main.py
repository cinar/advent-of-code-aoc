#
# Advent of Code 2021 - Day 4
#
import re

input_file = "sample.txt"

with open(input_file, "r") as file:
  parts = file.read().split("\n\n")
  drawns = [int(v) for v in parts[0].split(",")]
  boards = [[int(v) for v in re.findall("\d+", p)] for p in parts[1:]]

  for drawn in drawns:
    for board in boards:
      if drawn in board:
        i = board.index(drawn)
        board[i] = None
        print([1 if board[i] else 0 for i in range(i // 5, (i + 1) // 5)])

  print(drawns)
  print(boards[0])
