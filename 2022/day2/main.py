#
# Advent of Code 2022 - Day 2 - Part 1 and 2
#

input_file = "input2.txt"

# Rock - A - X - 1
# Paper - B - Y - 2
# Scissors - C - Z - 3

# Part 1
score = 0
for line in open(input_file, "r"):
  a, b = line.split()
  a = "ABC".index(a)
  b = "XYZ".index(b)

  score += (b + 1)
  
  if a == b:
    score += 3
  elif ((b + 1) % 3) != a:
    score += 6

print(f"Score b is {score}")
assert score == 12772

# Part 2
score = 0
for line in open(input_file, "r"):
  a, b = line.split()
  a = "ABC".index(a)

  if b == 'Y':
    score += (a + 1) + 3
  elif b == 'Z':
    score += (((a + 1) % 3) + 1) + 6
  else:
    score += (((a + 2) % 3) + 1)
    
print(f"Score b is {score}")
assert score == 11618
