#!/usr/bin/env python3

from collections import deque
from pathlib import Path
import grid


def read_lines_from_file(file_name):
    """Read lines from given file name."""
    return Path(file_name).read_text(encoding="utf-8").splitlines()

def main():
    lines = read_lines_from_file("input.txt")
    board = grid.Grid("".join(lines), len(lines[0]))

    start = board.find_index_of("S")
    board.set_index(start, "a")

    end = board.find_index_of("E")
    board.set_index(end, "z")

    candidates = deque([(set([start]), start)])
    min_steps = None

    while len(candidates) > 0:
        visited, current = candidates.popleft()

        if current == end:
            steps = len(visited)
            print(f"Found with steps {len(visited)}.")
            if not min_steps or min_steps > steps:
                min_steps = steps
            continue

        neighbours = set(board.orthogonal_neighbours(current)).difference(visited)

        closest = sorted(board.distance_to_index(end, neighbours), reverse=True)
        elevation = ord(board.at_index(current))

        for _, index in closest:
            if ord(board.at_index(index)) - elevation < 2:
                candidates.append((visited.union([index]), index))

    print(f"Steps {min_steps}.")

if __name__ == "__main__":
    main()
