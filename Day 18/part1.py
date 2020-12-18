import os, pathlib
import re 

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()


def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def replace(matcher):
    string = matcher.group(1)
    return str(do_math(string))
    
def do_math(string):
    exp = string.split(' ')
    left = exp.pop(0)
    while len(exp) > 0:
        right = exp.pop(0)
        if right == "+":
            op = add
        elif right == "*":
            op = mul
        else:
            left = op(int(left), int(right))
    return left


def process(exp):
    if '(' in exp:
        return process(re.sub('\(([^()]*)\)', replace, exp))
    return do_math(exp)


answers = []
for exp in inputs:
    answers.append(process(exp))

print(sum(answers))