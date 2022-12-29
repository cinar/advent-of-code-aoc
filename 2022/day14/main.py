from collections import defaultdict
from pathlib import Path

DATA = Path("input.txt").read_text(encoding="utf-8").splitlines()
SAND_START = (500, 0)


def pairwise(l):
    return zip(l, l[1:])


def print_grid(grid, min_x, max_x, max_y):
    print(
        "\n".join(
            "".join(grid[(x, y)] for x in range(min_x, max_x + 1))
            for y in range(0, max_y + 1)
        )
    )


def make_grid():
    grid = defaultdict(lambda: ".")

    for l in DATA:
        for c1, c2 in pairwise(l.split(" -> ")):
            x1, y1 = map(int, c1.split(",")[:2])
            x2, y2 = map(int, c2.split(",")[:2])
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[(x1, y)] = "#"
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[(x, y1)] = "#"

    return (
        grid,
        min(x for x, _ in grid.keys()),
        max(x for x, _ in grid.keys()),
        max(y for _, y in grid.keys()),
    )


def p1():
    grid, min_x, max_x, max_y = make_grid()
    x, y = SAND_START
    units = 0

    while min_x <= x <= max_x and y <= max_y:
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
    grid, _, _, max_y = make_grid()
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
