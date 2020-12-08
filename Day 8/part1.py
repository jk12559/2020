import os, pathlib

inputfile = os.path.join(pathlib.Path(__file__).parent, "input.txt")
inputs = open(inputfile, 'r').read().splitlines()

pointer = 0
visited = []
accumulator = 0
while pointer not in visited:
    visited.append(pointer)
    command = inputs[pointer]
    instruction, argument = command.split(" ")
    if instruction == "acc":
        accumulator += int(argument)
        pointer += 1
    elif instruction == "jmp":
        pointer += int(argument)
    elif instruction == "nop":
        pointer += 1

print(accumulator)
