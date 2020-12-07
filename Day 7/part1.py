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
        object_rule = re.compile("\d+ (.*) bags?")
        for obj in objects.split(", "):
            object_match = object_rule.match(obj)
            if object_match:
                thing = object_match.group(1)
                if thing in rules:
                    rules[thing].append(container)
                else:
                    rules[thing] = [container]
            else:
                print(rule)
                print(obj)
    else:
        print(rule)

bags = set()
stack = ["shiny gold"]
while len(stack) > 0:
    next_bag = stack.pop()
    if next_bag not in bags:
        stack.extend(rules[next_bag] if next_bag in rules else [])
        bags.add(next_bag)

print(len(bags))
