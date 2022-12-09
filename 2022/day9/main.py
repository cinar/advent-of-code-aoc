""" AoC 2022 Day 9 """
from pathlib import Path

#INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"


MOVE = {
    "U": Point(0, 1),
    "D": Point(0, -1),
    "L": Point(-1, 0),
    "R": Point(1, 0)
}


def calculate(rope):
    visited = set()
    for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
        direction, distance = line.split()
        for _ in range(int(distance)):
            rope[0] += MOVE[direction]
            for i in range(1, len(rope)):
                delta = rope[i-1] - rope[i]
                around = Point(min(1, max(-1, delta.x)),
                               min(1, max(-1, delta.y)))
                if delta != around:
                    rope[i] += around
            visited.add(rope[-1])

    show(rope, visited)
    print(len(visited))


def show(rope, visited):
    x = sorted(p.x for p in visited)
    y = sorted(p.y for p in visited)

    for i in range(y[-1], y[0] - 1, -1):
        row = ""
        for j in range(x[0], x[-1] + 1):
            p = Point(j, i)
            if p in rope:
                row += str(rope.index(p))
            elif p in visited:
                row += "#"
            else:
                row += "."
        print(row)


#
# Part 1
#
calculate([Point(0, 0)] * 2)

#
# Part 2
#
calculate([Point(0, 0)] * 10)
