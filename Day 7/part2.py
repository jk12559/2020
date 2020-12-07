import os, pathlib
import re

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

rules = dict()
main_rule = re.compile("(?P<container>.*) bags contain (?P<objects>.*)")
for rule in inputs:
    main_match = main_rule.match(rule)
    if main_match:
        container = main_match.group("container")
        objects = main_match.group("objects")
        object_rule = re.compile("(\d+) (.*) bags?")
        for obj in objects.split(", "):
            object_match = object_rule.match(obj)
            if object_match:
                count = int(object_match.group(1))
                thing = object_match.group(2)
                if container in rules:
                    rules[container].append((count, thing))
                else:
                    rules[container] = [(count, thing)]
            else:
                print(rule)
                print(obj)
    else:
        print(rule)


def count_inside(containers, name):
    bags = 0
    if name in rules:
        for count, bag in rules[name]:
            bags += count_inside(containers*count, bag)
    return bags + containers

print(count_inside(1, "shiny gold"))
