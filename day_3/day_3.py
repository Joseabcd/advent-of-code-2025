import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
input_path = os.path.join(script_dir, "input.txt")

with open(input_path, "r") as f:
    data = f.read()

bank_list = data.split()


# ------------------------------------------------------------
# Part 1
# ------------------------------------------------------------

total_jolts = 0
for bank in bank_list:
  p0, p1 = 0, 1
  for p in range(1, len(bank)):
    if bank[p] > bank[p0] and p < (len(bank) - 1):
      p0 = p
      p1 = p0 + 1
    elif bank[p] > bank[p1]:
      p1 = p
      if bank[p1] == '9':
        break
  cur_jolts = int(bank[p0] + bank[p1])
  total_jolts += cur_jolts

print(total_jolts)


# ------------------------------------------------------------
# Part 2
# ------------------------------------------------------------

k = 12
total_jolts = 0
for bank in bank_list:
  plist = []
  pstart = -1
  i = 0
  while i < k:
    pstart += 1
    plist += [pstart]
    for p in range(pstart + 1, len(bank) - (k - 1) + i):
      if bank[plist[i]] == '9':
        break
      if bank[p] > bank[plist[i]]:
        plist[i] = p
        pstart = p
    i += 1
  total_jolts += int(''.join(bank[elem] for elem in plist))

print(total_jolts)
