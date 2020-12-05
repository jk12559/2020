import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

def id_from_seat(seat):
    row_part = seat[0:7]
    seat_part = seat[7:]
    row_values = range(128)
    seat_values = range(8)
    for letter in row_part:
        size_to_keep = int(len(row_values) / 2)
        if letter == "F":
            row_values = row_values[:size_to_keep]
        elif letter == "B":
            row_values = row_values[size_to_keep:]
    for letter in seat_part:
        size_to_keep = int(len(seat_values) / 2)
        if letter == "L":
            seat_values = seat_values[:size_to_keep]
        if letter == "R":
            seat_values = seat_values[size_to_keep:]
    return row_values[0] * 8 + seat_values[0]

print(max([id_from_seat(x) for x in inputs]))
