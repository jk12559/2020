import os, pathlib
import re
import numpy as np
from functools import reduce

rulesfile = os.path.join(pathlib.Path(__file__).parent, "rules.txt")
rules = open(rulesfile, 'r').read().splitlines()

ticketsfile = os.path.join(pathlib.Path(__file__).parent, "tickets.txt")
tickets = open(ticketsfile, 'r').read().splitlines()

my_ticket = [53,101,83,151,127,131,103,61,73,71,97,89,113,67,149,163,139,59,79,137]

rule_pattern = re.compile('(.*): (\d+)-(\d+) or (\d+)-(\d+)')

rules_dict = dict()

for rule in rules:
    rule_match = rule_pattern.match(rule)
    range1 = list(range(int(rule_match.group(2)), int(rule_match.group(3))+1))
    range2 = list(range(int(rule_match.group(4)), int(rule_match.group(5))+1))
    rule_range = range1+range2
    rules_dict[rule_match.group(1)] = rule_range

all_valid_numbers = set([item for sublist in rules_dict.values() for item in sublist])

valid_tickets = []

for ticket_string in tickets:
    ticket = [int(x) for x in ticket_string.split(',')]
    should_add = True
    for number in ticket:
        if number not in all_valid_numbers:
            should_add = False
            break
    if should_add:
        valid_tickets.append(ticket)

def is_valid(column, range):
    for number in column:
        if number not in range:
            return False
    return True

ticket_array = np.array(valid_tickets)
possibilities = dict()
for rule, rule_range in rules_dict.items():
    possibilities[rule] = np.apply_along_axis(is_valid,0,ticket_array,rule_range)

results = dict()
while len(possibilities) > 0:
    for rule, possibility in possibilities.copy().items():
        if possibility.sum() == 1:
            results[rule] = np.where(possibility)[0][0]
            del possibilities[rule]
            for poss in possibilities.values():
                poss[results[rule]] = False

answer_values = []
for field, index in results.items():
    if "departure" in field:
        answer_values.append(my_ticket[index])

print(reduce(lambda x, y: x*y, answer_values))