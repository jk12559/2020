import os, pathlib
import numpy as np
import scipy.ndimage as image

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
room = open(inputfile, 'r').read()

def string_to_int(element):
    return int(element.replace('.', '-1').replace('L', '0').replace('#', '1'))

def int_to_string(element):
    return str(element).replace('-1', '.').replace('0', 'L').replace('1', '#')

def update_element(footprint):
    current = footprint[4]
    other = np.delete(footprint, 4)
    if current == 0 and np.count_nonzero(other == 1.0) == 0:
        return 1
    if current == 1 and np.count_nonzero(other == 1.0) >= 4:
        return 0
    return int(current)

grid = np.array([[string_to_int(x) for x in y] for y in room.splitlines()])

new_grid = grid
old_grid = np.zeros(grid.shape)
while not np.equal(old_grid, new_grid).all():
    old_grid = new_grid
    new_grid = image.generic_filter(old_grid, update_element, size = 3, cval = -1.0, mode = 'constant')

print(np.count_nonzero(new_grid == 1))