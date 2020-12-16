import os, pathlib
import re

rulesfile = os.path.join(pathlib.Path(__file__).parent, "rules.txt")
rules = open(rulesfile, 'r').read().splitlines()

ticketsfile = os.path.join(pathlib.Path(__file__).parent, "tickets.txt")
tickets = open(ticketsfile, 'r').read().splitlines()

rule_pattern = re.compile('(.*): (\d+)-(\d+) or (\d+)-(\d+)')

rules_dict = dict()

for rule in rules:
    rule_match = rule_pattern.match(rule)
    range1 = list(range(int(rule_match.group(2)), int(rule_match.group(3))+1))
    range2 = list(range(int(rule_match.group(4)), int(rule_match.group(5))+1))
    rule_range = range1+range2
    rules_dict[rule_match.group(1)] = rule_range

all_valid_numbers = set([item for sublist in rules_dict.values() for item in sublist])

invalid_nums = []
for ticket_string in tickets:
    ticket = [int(x) for x in ticket_string.split(',')]
    for number in ticket:
        if number not in all_valid_numbers:
            invalid_nums.append(number)

print(sum(invalid_nums))