import os, pathlib
import numpy as np

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
room = open(inputfile, 'r').read()

blah = [[x for x in y] for y in room.splitlines()]
grid = np.array(blah)

def get_left_seat(row, col):
    while col > 0:
        col -= 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None

def get_right_seat(row, col):
    while col < grid.shape[1]-1:
        col += 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None

def get_up_seat(row, col):
    while row > 0:
        row -= 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None

def get_down_seat(row, col):
    while row < grid.shape[0]-1:
        row += 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None

def get_up_right_seat(row, col):
    while row > 0 and col < grid.shape[1]-1:
        col += 1
        row -= 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None

def get_down_right_seat(row, col):
    while row < grid.shape[0]-1 and col < grid.shape[1]-1:
        row += 1
        col += 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None

def get_up_left_seat(row, col):
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None

def get_down_left_seat(row, col):
    while row < grid.shape[0]-1 and col > 0:
        row += 1
        col -= 1
        element = grid[row, col]
        if element == 'L':
            return row, col
    return None


relevant_seats = dict()
for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        if grid[row, col] == 'L':
            visible_seats = []
            visible_seats.append(get_left_seat(row, col))
            visible_seats.append(get_right_seat(row, col))
            visible_seats.append(get_up_seat(row, col))
            visible_seats.append(get_down_seat(row, col))
            visible_seats.append(get_up_right_seat(row, col))
            visible_seats.append(get_down_right_seat(row, col))
            visible_seats.append(get_up_left_seat(row, col))
            visible_seats.append(get_down_left_seat(row, col))
            relevant_seats[(row,col)] = visible_seats

new_grid = grid
old_grid = np.empty(grid.shape, grid.dtype)

def update_seat(row, col, grid):
    seats = relevant_seats[(row,col)]
    symbols = [grid[x[0], x[1]] for x in seats if x]
    count_occupied = symbols.count('#')
    current = grid[row,col]
    if current == 'L' and count_occupied == 0:
        return '#'
    if current == '#' and count_occupied >= 5:
        return 'L'
    else:
        return current
        
while not np.array_equal(old_grid, new_grid):
    old_grid = new_grid
    new_grid = np.empty(grid.shape, grid.dtype)
    for row in range(old_grid.shape[0]):
        for col in range(old_grid.shape[1]):
            if old_grid[row, col] == '.':
                new_grid[row, col] = '.'
            else:
                new_grid[row,col] = update_seat(row, col, old_grid)

print(np.count_nonzero(new_grid == '#'))