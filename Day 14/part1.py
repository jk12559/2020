import os, pathlib
import re 

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

mask_pattern = re.compile('mask = (\w{36})')
mem_pattern = re.compile('mem\[(\d*)\] = (\d*)')

mask = ''
mem = dict()
for line in inputs:
    mask_match = mask_pattern.match(line)
    mem_match = mem_pattern.match(line)
    if mask_match:
        mask = mask_match.group(1)
    elif mem_match:
        location = mem_match.group(1)
        value = mem_match.group(2)
        bin_value = format(int(value), "#038b")[2:]
        new_value = []
        for i in range(36):
            bit = mask[i]
            if bit != "X":
                new_value.append(bit)
            else:
                new_value.append(bin_value[i])
        value = int("0b{}".format(''.join(new_value)), 2)
        mem[location] = value

print(sum(mem.values()))
