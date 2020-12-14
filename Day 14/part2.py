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
        bin_location = format(int(location), "#038b")[2:]
        new_locations = ['']
        for i in range(36):
            bit = mask[i]
            if bit == "0":
                new_locations = [x + bin_location[i] for x in new_locations]
            elif bit == "1":
                new_locations = [x + '1' for x in new_locations]
            elif bit == "X":
                zero_loc = [x + '0' for x in new_locations]
                one_loc = [x + '1' for x in new_locations]
                new_locations = zero_loc + one_loc

        locations = [int("0b{}".format(x), 2) for x in new_locations]
        for location in locations:
            mem[location] = int(value)

print(sum(mem.values()))