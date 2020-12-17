start_condition = '''....#...
.#..###.
.#.#.###
.#....#.
...#.#.#
#.......
##....#.
.##..#.#'''

cubes = dict()
i = 0
j = 0
for char in start_condition:
    if char == '\n':
        j += 1
        i = 0
    else:
        cubes[(i, j, 0, 0)] = char
        i += 1

def get_neighbors(x,y,z,w):
    neighbors = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    neighbors.append((i, j, k, l))
    neighbors.remove((x,y,z,w))
    return neighbors

for cycle in range(6):
    active_cubes = dict(filter(lambda x: x[1] == "#", cubes.items()))

    x_min = min([x[0] for x in active_cubes.keys()])
    x_max = max([x[0] for x in active_cubes.keys()])
    y_min = min([x[1] for x in active_cubes.keys()])
    y_max = max([x[1] for x in active_cubes.keys()])
    z_min = min([x[2] for x in active_cubes.keys()])
    z_max = max([x[2] for x in active_cubes.keys()])
    w_min = min([x[3] for x in active_cubes.keys()])
    w_max = max([x[3] for x in active_cubes.keys()])

    x_range = range(x_min - 1, x_max + 2)
    y_range = range(y_min - 1, y_max + 2)
    z_range = range(z_min - 1, z_max + 2)
    w_range = range(w_min - 1, w_max + 2)

    old_cubes = cubes
    new_cubes = dict()
    for x in x_range:
        for y in y_range:
            for z in z_range:
                for w in w_range:
                    neighbors = get_neighbors(x,y,z,w)
                    active_neighbors = 0
                    for neighbor in neighbors:
                        if neighbor in active_cubes:
                            active_neighbors += 1
                    if (x,y,z,w) in active_cubes:
                        if active_neighbors in [2, 3]:
                            new_cubes[(x,y,z,w)] = "#"
                        else:
                            new_cubes[(x,y,z,w)] = "."
                    else:
                        if active_neighbors == 3:
                            new_cubes[(x,y,z,w)] = "#"
                        else:
                            new_cubes[(x,y,z,w)] = "."

    cubes = new_cubes

active_cubes = dict(filter(lambda x: x[1] == "#", cubes.items()))

print(len(active_cubes))


