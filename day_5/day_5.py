import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

range_specs, ingredient_ids = data.split('\n\n')
ingredient_ids = [int(id) for id in ingredient_ids.split()]
range_list = []
for spec in range_specs.split():
  left, right = spec.split('-')
  left, right = int(left), int(right)
  range_list += [range(left, right + 1)]


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

count = 0
for id in ingredient_ids:
  for r in range_list:
    if id in r:
      count += 1
      break

print(count)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------


# Materializing all the elements from the ranges crashes out of memory:

# fresh_ingredient_ids = set()
# for r in range_list:
#   fresh_ingredient_ids.update(set(r))
# print(len(fresh_ingredient_ids))


# Alternatively, compute the non-overlapping ranges based only on their left and right limits:

class Node:
  def __init__(self, range, prev=None, next=None):
    self.range = range
    self.prev = prev
    self.next = next
  def delete(self):
    prev, next = self.prev, self.next
    if self.next is not None:
      self.next.prev = prev
    if self.prev is not None:
      self.prev.next = next
    del self
    return (prev, next)
  def append(self, node):
    self.next = node
    node.prev = self


node = Node(range_list[0])
head = node
for r in range_list:
  node = head
  left, right = r[0], r[-1]
  while True:
    if (left < node.range[0]) and (right > node.range[-1]):
      prev, next = node.delete()
      if prev is None:
        if next is not None:
          head = next
          node = next
          continue
        else:
          head = Node(range(left, right + 1))
          break
      if next is None:
        prev.append(Node(range(left, right + 1)))
        break
    elif (left in node.range) and (right not in node.range):
      left = node.range[0]
      prev, next = node.delete()
      if prev is None:
        if next is not None:
          head = next
          node = next
          continue
        else:
          head = Node(range(left, right + 1))
          break
      if next is None:
        prev.append(Node(range(left, right + 1)))
        break
    elif (left not in node.range) and (right in node.range):
      right = node.range[-1]
      prev, next = node.delete()
      if prev is None:
        if next is not None:
          head = next
          node = next
          continue
        else:
          head = Node(range(left, right + 1))
          break
      if next is None:
        prev.append(Node(range(left, right + 1)))
        break
    elif (left not in node.range) and (right not in node.range):
      next = node.next
      if next is None:
        node.append(Node(range(left, right + 1)))
        break
    elif (left in node.range) and (right in node.range):
      break
    node = next

cur = head
total_range_lengths = 0
while cur is not None:
  total_range_lengths += len(cur.range)
  cur = cur.next

print(total_range_lengths)
