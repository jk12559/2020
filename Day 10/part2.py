import os, pathlib
from functools import reduce

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

adapters = [int(x) for x in inputs]

sorted_adapters = sorted(adapters)
sorted_adapters.insert(0, 0)
sorted_adapters.append(max(sorted_adapters)+3)
diffs = [sorted_adapters[i] - sorted_adapters[i-1] for i in range(1,len(sorted_adapters))]

segments = "".join([str(x) for x in diffs]).split('3')
def possibilities(segment):
    if len(segment) <= 1:
        return 1
    if len(segment) == 2:
        return 2
    if len(segment) == 3:
        return 4
    if len(segment) == 4:
        return 7
combos = map(possibilities, segments)
total = reduce(lambda x,y: x*y, combos)
print(total)