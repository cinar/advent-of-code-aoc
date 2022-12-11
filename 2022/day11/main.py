""" AoC 2022 Day 11. """
from dataclasses import dataclass
from math import prod
from pathlib import Path
from re import findall

#INPUT_FILE = "sample.txt"
INPUT_FILE = "input.txt"


class Monkey:
    """ Monkey object. """

    def __init__(self, lines):
        self.id = findall("\d+", lines[0])[0]
        self.items = [int(item) for item in findall("\d+", lines[1])]
        self.operation = lines[2][19:]
        self.divisible = int(findall("\d+", lines[3])[0])
        self.throw_true = findall("\d+", lines[4])[0]
        self.throw_false = findall("\d+", lines[5])[0]
        self.inspected = 0


def read_monkeys():
    """ Read monkeys from the input file. """
    monkeys = {}
    for section in Path(INPUT_FILE).read_text(encoding="utf-8").split("\n\n"):
        monkey = Monkey(section.splitlines())
        monkeys[monkey.id] = monkey

    return monkeys


def print_items(round, monkeys):
    """ Print items of monkeys. """
    print(f"After the round {round + 1}:")
    for id in sorted(monkeys):
        monkey = monkeys[id]
        print(f"Monkey {monkey.id}: {monkey.items}")


def print_inspected(monkeys):
    """ Print how many items inspected by each monkey. """
    for id in sorted(monkeys):
        monkey = monkeys[id]
        print(
            f"Monkey {monkey.id} inspected items {monkey.inspected} times.")


def print_business(monkeys):
    """ Print level of business. """
    active = sorted([monkey.inspected
                    for monkey in monkeys.values()], reverse=True)
    business = active[0] * active[1]
    print(f"The level of business is {business}.")


def calculate1():
    """ Part 1. """
    monkeys = read_monkeys()
    for round in range(20):
        for id in sorted(monkeys):
            monkey = monkeys[id]
            while monkey.items:
                old = monkey.items.pop(0)
                old = eval(monkey.operation) // 3
                if old % monkey.divisible == 0:
                    monkeys[monkey.throw_true].items.append(old)
                else:
                    monkeys[monkey.throw_false].items.append(old)
                monkey.inspected += 1

        print_items(round, monkeys)

    print_inspected(monkeys)
    print_business(monkeys)


def calculate2():
    """ Part 2. """
    monkeys = read_monkeys()
    limit = prod([monkey.divisible for monkey in monkeys.values()])

    for round in range(10000):
        for id in sorted(monkeys):
            monkey = monkeys[id]
            while monkey.items:
                old = monkey.items.pop(0)
                old = eval(monkey.operation) % limit
                if old % monkey.divisible == 0:
                    monkeys[monkey.throw_true].items.append(old)
                else:
                    monkeys[monkey.throw_false].items.append(old)
                monkey.inspected += 1

    print_business(monkeys)


calculate1()
calculate2()
