#!/usr/bin/env python3

from collections import deque
from pathlib import Path
import sys

sys.path.append("../")

from grid import Grid


def read_lines_from_file(file_name):
    """Read lines from given file name."""
    return Path(file_name).read_text(encoding="utf-8").splitlines()


def p1():
    lines = read_lines_from_file("input.txt")
    board = Grid("".join(lines), len(lines[0]))

    start = board.find_index_of("S")
    board.set_index(start, "a")

    end = board.find_index_of("E")
    board.set_index(end, "z")

    candidates = deque([(0, start)])
    visited = {}

    while len(candidates) > 0:
        steps, current = candidates.popleft()
        if current in visited:
            continue

        visited[current] = steps

        neighbours = set(board.orthogonal_neighbours(current))

        closest = sorted(board.distance_to_index(end, neighbours), reverse=True)
        elevation = ord(board.at_index(current))

        for _, index in closest:
            if ord(board.at_index(index)) - elevation < 2:
                candidates.append((steps + 1, index))

    print(f"P1 {visited[end]}.")


def p2():
    lines = read_lines_from_file("input.txt")
    board = Grid("".join(lines), len(lines[0]))

    start = board.find_index_of("S")
    board.set_index(start, "a")

    end = board.find_index_of("E")
    board.set_index(end, "z")

    candidates = deque([(0, a) for a in board.find_index_of_all("a")])
    visited = {}

    while len(candidates) > 0:
        steps, current = candidates.popleft()
        if current in visited:
            continue

        visited[current] = steps

        neighbours = set(board.orthogonal_neighbours(current))

        closest = sorted(board.distance_to_index(end, neighbours), reverse=True)
        elevation = ord(board.at_index(current))

        for _, index in closest:
            if ord(board.at_index(index)) - elevation < 2:
                candidates.append((steps + 1, index))

    print(f"P2 {visited[end]}.")


if __name__ == "__main__":
    p1()
    p2()
