import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()
busses = inputs[1].split(',')

values = []
for i in range(len(busses)):
    if busses[i] != 'x':
        values.append((i, int(busses[i])))

left = values.pop(0)
offset = 0
while len(values) != 0:
    right = values.pop(0)
    for i in range(right[1]):
        if (offset + left[1] * i + right[0]) % right[1] == 0:
            offset = left[1] * i + offset
            left = (0, left[1] * right[1])
            break


print(offset)
# for i in range(13):
#     if (17 * i + 2) % 13 == 0:
#         offset = 17 * i
#         break
# for i in range(19):
#     if (offset + (13*17 * i) +3) % 19 == 0:
#         break

# print(13*17*i+offset)