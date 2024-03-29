""" AoC 2022 Day 16. """

import collections
import functools
import pathlib
import re

Valve = collections.namedtuple("Valve", ["name", "rate", "tunnels"])

valves = {
    name: Valve(name, int(rate), tunnels.split(", "))
    for name, rate, tunnels in re.findall(
        "Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? ([A-Z ,]+)",
        pathlib.Path("input.txt").read_text(encoding="utf-8"),
        re.MULTILINE,
    )
}


@functools.lru_cache(maxsize=None)
def dp1(name, minutes, opened):
    if minutes <= 0:
        return 0

    valve = valves[name]

    option1 = max(dp1(n, minutes - 1, opened) for n in valve.tunnels)
    if valve.rate == 0 or name in opened:
        return option1

    opened = opened.union({name})
    option2 = (valve.rate * (minutes - 1)) + max(
        dp1(n, minutes - 2, opened) for n in valve.tunnels
    )

    return max(option1, option2)


@functools.lru_cache(maxsize=1024 * 1024)
def dp2(name, minutes, opened):
    if minutes <= 0:
        return 0

    valve = valves[name]

    option0 = dp1("AA", 26, opened)

    option1 = max(dp2(n, minutes - 1, opened) for n in valve.tunnels)
    if valve.rate == 0 or name in opened:
        return max(option0, option1)

    opened = opened.union({name})
    option2 = (valve.rate * (minutes - 1)) + max(
        dp2(n, minutes - 2, opened) for n in valve.tunnels
    )

    return max(option0, option1, option2)


def p1():
    print("p1", dp1("AA", 30, frozenset()))


def p2():
    print("p2", dp2("AA", 26, frozenset()))


p1()

p2()
