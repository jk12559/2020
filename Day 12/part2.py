import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

ship_ew = 0
ship_ns = 0
wp_ew = 10
wp_ns = 1

def rotate_left_90():
    global wp_ns, wp_ew
    new_ns = wp_ew
    new_ew = -1 * wp_ns
    wp_ns = new_ns
    wp_ew = new_ew
    
def rotate_right_90():
    global wp_ns, wp_ew
    new_ns = -1 * wp_ew
    new_ew = wp_ns
    wp_ns = new_ns
    wp_ew = new_ew

def rotate(direction, angle):
    turns = int(angle / 90)
    if direction == "L":
        for i in range(turns):
            rotate_left_90()
    else:
        for i in range(turns):
            rotate_right_90()

def translate(direction, distance):
    global wp_ns, wp_ew
    if direction == "N":
        wp_ns += distance
    elif direction == "S":
        wp_ns -= distance
    elif direction == "E":
        wp_ew += distance
    elif direction == "W":
        wp_ew -= distance

def move_ship(times):
    global ship_ns, ship_ew
    ship_ns = ship_ns + times * wp_ns
    ship_ew = ship_ew + times * wp_ew

for move in inputs:
    action = move[0]
    amount = int(move[1:])
    if action in "NSEW":
        translate(action, amount)
    elif action in "LR":
        rotate(action, amount)
    elif action == "F":
        move_ship(amount)

print(abs(ship_ew)+abs(ship_ns))