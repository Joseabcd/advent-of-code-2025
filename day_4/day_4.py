import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

mask = [[int(c.replace('@', '1').replace('.', '0')) for c in line] for line in data.split()]


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

accessible_rolls = 0
m, n = len(mask), len(mask[0])
for i in range(m):
  for j in range(n):
    if mask[i][j]:
      adjacent_rolls = 0
      if i > 0:
        adjacent_rolls += mask[i - 1][j]
        if j > 0:
          adjacent_rolls += mask[i - 1][j - 1]
        if j < n - 1:
          adjacent_rolls += mask[i - 1][j + 1]
      if i < m - 1:
        adjacent_rolls += mask[i + 1][j]
        if j > 0:
          adjacent_rolls += mask[i + 1][j - 1]
        if j < n - 1:
          adjacent_rolls += mask[i + 1][j + 1]
      if j > 0:
        adjacent_rolls += mask[i][j - 1]
      if j < n - 1:
        adjacent_rolls += mask[i][j + 1]
      
      if adjacent_rolls < 4:
        accessible_rolls += 1
      
print(accessible_rolls)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------
