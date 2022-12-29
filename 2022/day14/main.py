from collections import defaultdict
from itertools import product
from pathlib import Path

DATA = Path("input.txt").read_text(encoding="utf-8").splitlines()
SAND_START = (500, 0)


def print_grid(grid, max_y, min_x, max_x):
    print(
        "\n".join(
            "".join(grid[(x, y)] for x in range(min_x, max_x + 1))
            for y in range(0, max_y + 1)
        )
    )


def make_grid():
    grid = defaultdict(lambda: ".")
    max_y = 0

    for l in DATA:
        c = l.split(" -> ")
        for c1, c2 in zip(c, c[1:]):
            x1, y1 = map(int, c1.split(",")[:2])
            x2, y2 = map(int, c2.split(",")[:2])
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))
            max_y = max(max_y, y2)
            for x, y in product(range(x1, x2 + 1), range(y1, y2 + 1)):
                grid[(x, y)] = "#"

    return (grid, max_y)


def p1():
    grid, max_y = make_grid()
    x, y = SAND_START
    units = 0

    while y <= max_y:
        if grid[(x, y + 1)] == ".":
            y += 1
        elif grid[(x - 1, y + 1)] == ".":
            x -= 1
            y += 1
        elif grid[(x + 1, y + 1)] == ".":
            x += 1
            y += 1
        else:
            grid[(x, y)] = "o"
            units += 1
            x, y = SAND_START

    print("P1:", units)


def p2():
    grid, max_y = make_grid()
    x, y = SAND_START
    units = 0

    while grid[(x, y)] == ".":
        if y < max_y + 1:
            if grid[(x, y + 1)] == ".":
                y += 1
                continue
            elif grid[(x - 1, y + 1)] == ".":
                x -= 1
                y += 1
                continue
            elif grid[(x + 1, y + 1)] == ".":
                x += 1
                y += 1
                continue

        grid[(x, y)] = "o"
        units += 1
        x, y = SAND_START

    print("P2:", units)


p1()
p2()
