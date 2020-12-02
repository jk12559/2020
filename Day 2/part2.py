import os, pathlib
import re

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').readlines()

pattern = re.compile("(?P<min>\d*)-(?P<max>\d*) (?P<reqLetter>\w): (?P<password>\w*)")

def password_is_valid(min, max, reqLetter, password):
    valid = False
    if password[int(min)-1] == reqLetter:
        valid = ~valid
    if password[int(max)-1] == reqLetter:
        valid = ~valid
    return valid

count = 0
for input in inputs:
    match = re.match(pattern, input)
    minimum = match.group("min")
    maximum = match.group("max")
    reqLetter = match.group("reqLetter")
    password = match.group("password")
    if password_is_valid(minimum, maximum, reqLetter, password):
        count += 1

print(count)
