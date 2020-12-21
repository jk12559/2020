import os, pathlib
import re

inputfile = os.path.join(pathlib.Path(__file__).parent, "grammar_input.txt")
grammar_inputs = open(inputfile, 'r').read().splitlines()
inputfile = os.path.join(pathlib.Path(__file__).parent, "messages_input.txt")
messages_inputs = open(inputfile, 'r').read().splitlines()
# grammar_inputs = '''0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"'''.splitlines()
# messages_inputs='''ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb'''.splitlines()

rule_pattern = re.compile('(\d+): (.*)')

rules = dict()

for rule in grammar_inputs:
    rule_match = rule_pattern.match(rule)
    rules[rule_match.group(1)] = [x.strip().split(' ') for x in rule_match.group(2).split('|')]

def is_terminal(rule):
    if '"' in rules[rule][0][0]:
        return True
    return False

def is_valid(rule, letters):
    if len(letters) == 0:
        return False, ''
    if is_terminal(rule):
        if letters[0] in rules[rule][0][0]:
            return True, letters[1:]
        return False, letters
    options = rules[rule]
    for option in options:
        inner_option = option[:]
        while len(inner_option) > 0:
            next_rule = inner_option.pop(0)
            valid, remainder = is_valid(next_rule, letters)
            if valid:
                letters = remainder
            else:
                break
        if valid:
            return True, remainder
    return False, letters

def is_fully_valid(rule,letters):
    valid, remainder = is_valid(rule,letters)
    if valid and remainder == '':
        return True
    return False

print(sum([is_fully_valid('0', x) for x in messages_inputs],messages_inputs))