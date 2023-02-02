import itertools
import pathlib

pattern = itertools.cycle(
  pathlib.Path("2022/day17/input.txt").read_text(encoding="utf-8"))

shapes = itertools.cycle([[(2, 0), (3, 0), (4, 0), (5, 0)],
                          [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],
                          [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
                          [(2, 0), (2, 1), (2, 2), (2, 3)],
                          [(2, 0), (3, 0), (2, 1), (3, 1)]])

height = 1
width = 7

bucket = {(x, 0) for x in range(0, width)}


def is_valid(shape):
  return all((p not in bucket) and (0 <= p[0] < width) for p in shape)

for rock in range(1, 2023):
  shape = [(p[0], p[1] + height + 3) for p in next(shapes)]

  while True:
    delta = -1 if next(pattern) == "<" else 1
    
    new_shape = [(p[0] + delta, p[1]) for p in shape]
    if is_valid(new_shape):
      shape = new_shape

    new_shape = [(p[0], p[1] - 1) for p in shape]
    if is_valid(new_shape):
      shape = new_shape
    else:
      bucket.update(shape)
      height = max(height, max(p[1] for p in shape) + 1)
      break

def print_bucket():
  for y in range(height, -1, -1):
    for x in range(0, width):
      if (x, y) in bucket:
        print("#", end="")
      else:
        print(".", end="")
    print("")

print("Height", height - 1)

