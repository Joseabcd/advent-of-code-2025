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

raw_operands, _, raw_operators = data.rpartition("\n")

operands_lines = raw_operands.splitlines()
operands = [line.split() for line in operands_lines]
operands = np.asarray(operands, dtype=int)

operators = raw_operators.split()

mult_mask = [op == '*' for op in operators]
add_mask = [op == '+' for op in operators]

grand_total = np.sum(np.multiply.reduce(operands[:, mult_mask])) + \
  np.sum(np.add.reduce(operands[:, add_mask]))

print(grand_total)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------

# Code below doesn't assume equal-sized problems, even though the given puzzle input turned out to contain only 1000-sized problems

def transpose_flat_matrix(flat_matrix, nrows, ncols):
  matrix = flat_matrix.reshape((nrows, ncols))
  matrix_t = matrix.T
  flat_matrix_t = matrix_t.flatten()
  return flat_matrix_t


ncols = raw_operands.find("\n")
nrows = raw_operands.count("\n") + 1

char_matrix = np.asarray([raw_operands], dtype="S").view("S1")  # equivalent to (but more performant than) np.asarray(list(raw_operands), dtype="S1")

newline_positions = [ncols + i * ncols + i for i in range(nrows - 1)]
char_matrix = np.delete(char_matrix, newline_positions)

char_matrix_t = transpose_flat_matrix(char_matrix, nrows, ncols)

str_matrix = char_matrix_t.view("S%d" % nrows)  # group into a string the chars from each column

problem_separator = b' ' * nrows  # problems are separated by a column of whitespace
separator_positions, = np.nonzero(str_matrix == problem_separator)
problems =np.split(str_matrix, separator_positions)
problems[1:] = map(lambda a: np.delete(a, 0), problems[1:])  # trim separators

grand_total = 0
for prob, op in zip(problems, operators):
  if op == '*':
    grand_total += np.multiply.reduce(np.asarray(prob, dtype=int))
  elif op == '+':
    grand_total += np.add.reduce(np.asarray(prob, dtype=int))

print(grand_total)
