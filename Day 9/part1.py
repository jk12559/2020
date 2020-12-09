import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

def get_possible_sums(values):
    possibilities = set()
    while len(values) > 0:
        value_to_consider = values.pop()
        possibilities = possibilities.union(set([value_to_consider + x for x in values if x is not value_to_consider]))
    return possibilities

numbers = [int(x) for x in inputs]

for i in range(25, len(numbers)):
    possibilities = get_possible_sums(numbers[i-25:i])
    if numbers[i] not in possibilities:
        break

result = numbers[i]
print(result)