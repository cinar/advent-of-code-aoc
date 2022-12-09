""" AoC 2022 Day 9 """
from pathlib import Path

INPUT_FILE = "sample.txt"
#INPUT_FILE = "input.txt"

#
# Part 1
#
h = (0, 0)
t = (0, 0)
v = set(t)

for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    c, n = line.split()
    n = int(n)

    if c == "R":
        h = (h[0] + n, h[1])
        p = [(t[0] + x, h[1]) for x in range(1, abs(h[0] - t[0]))]
    elif c == "U":
        h = (h[0], h[1] + n)
        p = [(h[0], t[1] + x) for x in range(1, abs(h[1] - t[1]))]
    elif c == "L":
        h = (h[0] - n, h[1])
        p = [(t[0] - x, h[1]) for x in range(1, abs(h[0] - t[0]))]
    elif c == "D":
        h = (h[0], h[1] - n)
        p = [(h[0], t[1] - x) for x in range(1, abs(h[1] - t[1]))]

    if len(p) > 0:
        t = p[-1]
        v.update(p)

    #print(f"{c} {n} - h{h} t{t}")
    #print(f"{p}\n")

print(len(v))

#
# Part 2
#
INPUT_FILE = "sample2.txt"
#INPUT_FILE = "input.txt"

k = [(0, 0)] * 10
v = set(k[-1])

for line in Path(INPUT_FILE).read_text(encoding="utf-8").splitlines():
    c, n = line.split()

    print(k)
    for i in range(int(n)):
        h = k[0]

        if c == "R":
            h = (h[0] + 1, h[1])
        elif c == "U":
            h = (h[0], h[1] + 1)
        elif c == "L":
            h = (h[0] - 1, h[1])
        elif c == "D":
            h = (h[0], h[1] - 1)

        k[0] = h

        for j in range(len(k) - 1):
            h = k[j]
            t = k[j+1]

            if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
                if c == "R":
                    t = (t[0] + 1, h[1])
                elif c == "U":
                    t = (h[0], t[1] + 1)
                elif c == "L":
                    t = (t[0] - 1, h[1])
                elif c == "D":
                    t = (h[0], t[1] - 1)

                k[j+1] = t

                if j == len(k) - 2:
                    v.add(t)

print(len(v))
