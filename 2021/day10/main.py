""" AoC 2021 Day 10. """
from pathlib import Path

#INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"

OPENING = ("(", "[", "{", "<")
CLOSING = (")", "]", "}", ">")
ILLEGAL_POINTS = (3, 57, 1197, 25137)
COMPLETE_POINT = (1, 2, 3, 4)

complete_scores = []
illegal_score = 0
for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    stack = []
    illegal = False
    for c in line:
        if c in OPENING:
            stack.append(c)
        elif c in CLOSING:
            e = CLOSING[OPENING.index(stack.pop())]
            if e != c:
                print(f"{line} - Expected {e}, but found {c} instead.")
                illegal_score += ILLEGAL_POINTS[CLOSING.index(c)]
                illegal = True
                break

    if illegal or not stack:
        continue

    print(f"{line} - Complete by adding ", end="")
    complete_score = 0

    while stack:
        e = CLOSING[OPENING.index(stack.pop())]
        complete_score = (complete_score * 5) + \
            COMPLETE_POINT[CLOSING.index(e)]
        print(e, end="")

    print(f" (score {complete_score}).")
    complete_scores.append(complete_score)

complete_scores.sort()
middle_score = complete_scores[len(complete_scores) // 2]

print(f"Illegal score is {illegal_score}.")
print(f"Middle complete score {middle_score}.")
