import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().split("\n\n")

group_yes = 0
for group in inputs:
    answer_set = set()
    for person in group.splitlines():
        for question in person:
            answer_set.add(question)
    group_yes += len(answer_set)
print(group_yes)