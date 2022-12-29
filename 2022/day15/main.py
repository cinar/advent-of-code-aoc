""" AoC 2022 Day 15. """

from pathlib import Path
from re import findall


def md(x1, y1, x2, y2):
    """Returns the Manhattan Distance for the given points."""
    return abs(x1 - x2) + abs(y1 - y2)


DATA = Path("input.txt").read_text(encoding="utf-8").splitlines()
POS = [tuple(int(p) for p in findall(r"\-?\d+", l)) for l in DATA]

S = [(sx, sy, md(sx, sy, bx, by)) for sx, sy, bx, by in POS]
B = set((bx, by) for _, _, bx, by in POS)


def p1():
    MIN_X = min(sx - d for sx, _, d in S)
    MAX_X = max(sx + d for sx, _, d in S)

    Y = 2000000
    covered = 0

    for x in range(MIN_X, MAX_X + 1):
        if (x, Y) in B:
            continue
        for sx, sy, d in S:
            if d >= md(sx, sy, x, Y):
                covered += 1
                break

    print("P1:", covered)


def p2():
    UPPER = 4000000

    for sx, sy, d in S:
        for nx in range(d + 2):
            ny = (d + 1) - nx
            for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                x = sx + (dx * nx)
                y = sy + (dy * ny)

                if (x, y) in B:
                    continue

                if not (0 <= x <= UPPER and 0 <= y <= UPPER):
                    continue

                covered = False
                for ox, oy, od in S:
                    if md(ox, oy, x, y) <= od:
                        covered = True
                        break

                if not covered:
                    print("P2:", (x, y))
                    print("P2:", (x * UPPER + y))
                    return


p1()
p2()
