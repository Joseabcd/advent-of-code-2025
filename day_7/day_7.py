import os
import sys


script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

width = data.find('\n')
split_count = 0
x_set = set([data.find('S')]) # beam horizontal positions
k = 2
while k * width < len(data):
  x_set_copy = x_set.copy()
  start = k * (width + 1) - 1
  end = start + width
  while (idx:=data.find('^', start, end)) != -1:
    x = idx - k * (width + 1)
    if x in x_set_copy:  # if collision
      split_count += 1
      x_set.remove(x)
      if x > 0:
        x_set.add(x - 1)
      if x < width - 1:
        x_set.add(x + 1)
    start = idx + 1
  k += 2

print(split_count)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------

