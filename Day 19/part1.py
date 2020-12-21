import os, pathlib
import re

inputfile = os.path.join(pathlib.Path(__file__).parent, "grammar_input.txt")
grammar_inputs = open(inputfile, 'r').read().splitlines()
inputfile = os.path.join(pathlib.Path(__file__).parent, "messages_input.txt")
messages_inputs = open(inputfile, 'r').read().splitlines()

rule_pattern = re.compile('(\d+): (.*)')

rules = dict()

for rule in grammar_inputs:
    rule_match = rule_pattern.match(rule)
    rules[rule_match.group(1)] = [x.strip().split(' ') for x in rule_match.group(2).split('|')]

def is_terminal(rule):
    if '"' in rule[0]:
        return True
    return False

def is_valid(rule, letters):
    if len(rule) == 0 and len(letters) == 0:
        return True
    if len(rule) > 0 and len(letters) == 0:
        return False
    if len(rule) == 0 and len(letters) > 0:
        return False
    inner_rule = rule[:]
    next_value = inner_rule.pop(0)
    if is_terminal(next_value):
        if letters[0] in next_value:
            return is_valid(inner_rule, letters[1:])
        return False
    options = rules[next_value]
    for option in options:
        inner_option = option[:]
        inner_option.extend(inner_rule)
        valid = is_valid(inner_option, letters)
        if valid:
            return True
    return False

print(sum([is_valid(rules['0'][0], x) for x in messages_inputs]))