import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

ew = 0
ns = 0
facings = ['E', 'S', 'W', 'N']
facing = 0

def rotate(direction, angle):
    global facing
    turns = int(angle / 90)
    if direction == "L":
        turns *= -1
    facing = (facing + turns) % 4

def translate(direction, distance):
    global ns, ew
    if direction == "N":
        ns += distance
    elif direction == "S":
        ns -= distance
    elif direction == "E":
        ew += distance
    elif direction == "W":
        ew -= distance


for move in inputs:
    action = move[0]
    amount = int(move[1:])
    if action in "NSEW":
        translate(action, amount)
    elif action in "LR":
        rotate(action, amount)
    elif action == "F":
        direction = facings[facing]
        translate(direction, amount)

print(ew+ns)