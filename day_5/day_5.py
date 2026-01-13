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

class LinkedList:
  def __init__(self, head):
    self.head = head
    self.cur = head
    self.aux = None  # keeps track of the next node when the head is deleted and self.cur becomes None

  def get_current_node(self):
    return self.cur

  def move_to_next(self):
    if self.cur is not None:
      self.cur = self.cur.next
    else:
      self.cur = self.aux

  def move_to_head(self):
    self.cur = self.head

  def delete_current_node(self):
    prev, next = self.cur.prev, self.cur.next
    is_head = prev is None
    if not is_head:
      prev.next = next      
    if next is not None:
      next.prev = prev
    del self.cur
    self.cur = prev
    if is_head:
      self.head = next
      self.aux = next

  def append(self, node):
    if self.cur is None:
      self.head = node
    else:
      self.cur.next = node
    node.prev = self.cur

  def is_end(self):
    if self.cur is None:
      return self.aux is None
    return self.cur.next is None


lst = LinkedList(Node(range_list[0]))
for r in range_list:
  left, right = r[0], r[-1]
  lst.move_to_head()
  while True:
    node = lst.get_current_node()
    if (left in node.range) and (right in node.range):
      break
    elif (left < node.range[0]) and (right > node.range[-1]):
      lst.delete_current_node()
    elif (left in node.range) and (right not in node.range):
      left = node.range[0]
      lst.delete_current_node()
    elif (left not in node.range) and (right in node.range):
      right = node.range[-1]
      lst.delete_current_node()

    if lst.is_end():
      lst.append(Node(range(left, right + 1)))
      break
    else:
      lst.move_to_next()

lst.move_to_head()
total_range_lengths = 0
while lst.get_current_node() is not None:
  total_range_lengths += len(lst.get_current_node().range)
  lst.move_to_next()

print(total_range_lengths)
