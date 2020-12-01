import sys, os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').readlines()
inputvalues = [int(x) for x in inputs]

inputvalues.sort()

head = 0
mid = head + 1
tail = len(inputvalues) - 1
while head < tail:
    head_value = inputvalues[head]
    mid_value = inputvalues[mid]
    tail_value = inputvalues[tail]
    total = head_value + mid_value + tail_value
    if total > 2020:
        inputvalues.pop()
        tail -= 1
    else:
        while total < 2020:
            mid += 1
            mid_value = inputvalues[mid]
            total = head_value + mid_value + tail_value
        if total == 2020:
            break
        head += 1
        mid = head + 1
    

print("Value 1: {}".format(head_value))
print("Value 2: {}".format(mid_value))
print("Value 3: {}".format(tail_value))
print("Product: {}".format(head_value*mid_value*tail_value))
