import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().split("\n\n")

group_yes = 0
for group in inputs:
    answer_set = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s','t','u','v','w','x','y','z'])
    for person in group.splitlines():
        person_set = set([x for x in person])
        answer_set = answer_set.intersection(person_set)
    group_yes += len(answer_set)
print(group_yes)