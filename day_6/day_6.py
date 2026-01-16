import os
import sys
import numpy as np


script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

lines = data.splitlines()

operators = lines[-1].split()
operands = [l.split() for l in lines[:-1]]
operands = np.asarray(operands, dtype=int)

mult_mask = [op == '*' for op in operators]
add_mask = [op == '+' for op in operators]

grand_total = np.sum(np.multiply.reduce(operands[:, mult_mask])) + \
  np.sum(np.add.reduce(operands[:, add_mask]))

print(grand_total)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------
