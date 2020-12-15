starting = [16,11,15,0,1,7]

def get_result(start):
    visited = dict()
    for i in range(len(start)):
        current = start[i]
        visited[current] = i
    next_num = 0
    while i < 29999999:
        current = next_num
        if current not in visited:
            next_num = 0
        else:
            last_turn = visited[current]
            next_num = i + 1 - last_turn
        i += 1
        visited[current] = i
    return current



print(get_result(starting))