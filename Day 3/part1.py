import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

grid={}
grid_width = len(inputs[0])
grid_height = len(inputs)
print(inputs)
print(grid_height)
print(grid_width)
for row in range(grid_height):
    for column in range(grid_width):
        grid[(column, row)] = inputs[row][column]

current_row = 0
current_column = 0
trees = 0
while current_row < grid_height:
    spot = grid[(current_column, current_row)]
    if spot == "#":
        trees += 1
    current_column = (current_column + 3) % grid_width
    current_row += 1

print(trees)
    