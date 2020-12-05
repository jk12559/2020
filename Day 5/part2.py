from part1 import id_from_seat, inputs

ids = [id_from_seat(x) for x in inputs]
ids.sort()

prev_id = ids[0]
for id in ids[1:]:
    if id == prev_id + 1:
        prev_id = id
    else:
        break

print(prev_id + 1)