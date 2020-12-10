import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

numbers = [int(x) for x in inputs]

def count_diffs(adapters):
    sorted_adapters = sorted(adapters)
    sorted_adapters.insert(0, 0)
    sorted_adapters.append(max(sorted_adapters)+3)
    diffs = [sorted_adapters[i] - sorted_adapters[i-1] for i in range(1,len(sorted_adapters))]
    return diffs.count(1), diffs.count(3)

result = count_diffs(numbers)
print(result)
print(result[0] * result[1])