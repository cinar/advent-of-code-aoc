from ast import literal_eval
from pathlib import Path
from functools import cmp_to_key
from math import prod

DATA = Path("input.txt").read_text(encoding="utf-8")


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l - r
    elif isinstance(l, list) and isinstance(r, list):
        for a, b in zip(l, r):
            if result := compare(a, b):
                return result
        return len(l) - len(r)
    elif isinstance(l, list):
        return compare(l, [r])
    else:
        return compare([l], r)


def p1():
    pairs = [[literal_eval(l) for l in p.splitlines()] for p in DATA.split("\n\n")]

    correct = [i for i, (l, r) in enumerate(pairs, start=1) if compare(l, r) < 0]
    print("P1:", sum(correct))


def p2():
    pairs = [literal_eval(l) for l in DATA.splitlines() if len(l) > 0]
    dividers = [[[2]], [[6]]]
    pairs.extend(dividers)

    validated = sorted(pairs, key=cmp_to_key(compare))
    print("P2:", prod([validated.index(d) + 1 for d in dividers]))


p1()
p2()
