import os
import sys


script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

width = data.find('\n')


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

x_set = set([data.find('S')]) # beam horizontal positions

split_count = 0
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

# similar as before, but now multiple beams from different worlds
# can coexist in the same position w/o merging into one

x_counts = [0] * width
idx0 = data.find('S')
x_counts[idx0] = 1

split_count = 0
k = 2
while k * width < len(data):
  x_counts_copy = x_counts.copy()
  start = k * (width + 1) - 1
  end = start + width
  while (idx:=data.find('^', start, end)) != -1:
    x = idx - k * (width + 1)
    if x_counts_copy[x]:  # if collision
      split_count += x_counts_copy[x]
      x_counts[x] -= x_counts_copy[x]
      if x > 0:
        x_counts[x - 1] += x_counts_copy[x]
      if x < width - 1:
        x_counts[x + 1] += x_counts_copy[x]
    start = idx + 1
  k += 2

print(1 + split_count)

