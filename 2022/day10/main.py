""" AoC 2022 Day 10. """
from pathlib import Path

#INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"

#
# Part 1
#
signals = 0
cycles = 0
x = 1
for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    new_x = x
    need = 1

    if line.startswith("addx"):
        new_x += int(line.split()[1])
        need = 2

    for i in range(need):
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            signal = x * cycles
            signals += signal
            print(f"Strength at {cycles} is {signal}.")

    x = new_x

print(f"Total signals is {signals}.")

#
# Part 2
#
cycles = 0
x = 1
for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    new_x = x
    need = 1

    if line.startswith("addx"):
        new_x += int(line.split()[1])
        need = 2

    for i in range(need):
        column = cycles % 40
        if column == 0:
            print("")

        print("#" if column in [x-1, x, x+1] else " ", end="")
        cycles += 1

    x = new_x

print("")
