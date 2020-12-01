import sys, os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').readlines()
inputvalues = [int(x) for x in inputs]

inputvalues.sort()

head = 0
tail = len(inputvalues) - 1
while head < tail:
    head_value = inputvalues[head]
    tail_value = inputvalues[tail]
    total = head_value + tail_value
    if total > 2020:
        inputvalues.pop()
        tail -= 1
    elif total < 2020:
        head += 1
    else:
        break

print("Value 1: {}".format(head_value))
print("Value 2: {}".format(tail_value))
print("Product: {}".format(head_value*tail_value))
