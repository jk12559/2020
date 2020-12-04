import os, pathlib
from Passport import Passport

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().split("\n\n")

print(sum([Passport(x).is_valid() for x in inputs]))
