""" AoC 2021 Day 10. """
from pathlib import Path

#INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"

OPENING = ("(", "[", "{", "<")
CLOSING = (")", "]", "}", ">")
POINTS = (3, 57, 1197, 25137)

score = 0
for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    stack = []
    for c in line:
        if c in OPENING:
            stack.append(c)
        elif c in CLOSING:
            e = CLOSING[OPENING.index(stack.pop())]
            if e != c:
                score += POINTS[CLOSING.index(c)]
                print(f"{line} - Expected {e}, but found {c} instead.")
                break

print(f"Score {score}.")
