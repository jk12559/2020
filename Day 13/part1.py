import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

time = inputs[0]
busses = [int(x) for x in inputs[1].split(',') if x != "x"]

wait_times = sorted(list(zip(busses, [x-(int(time) % x) for x in busses])), key=lambda x: x[1])

print(wait_times[0][0] * wait_times[0][1])
