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

def run_program(commands):
    pointer = 0
    visited = []
    accumulator = 0
    while pointer not in visited:
        visited.append(pointer)
        command = commands[pointer]
        instruction, argument = command.split(" ")
        if instruction == "acc":
            accumulator += int(argument)
            pointer += 1
        elif instruction == "jmp":
            pointer += int(argument)
        elif instruction == "nop":
            pointer += 1
        if pointer == len(commands):
            return accumulator
        if pointer > len(commands):
            return False
    return False

for location in reversed(visited):
    revised_inputs = inputs[:]
    command = inputs[location]
    instruction, argument = command.split(" ")
    if instruction == "jmp":
        revised_inputs[location] = "nop %s" % (argument)
    elif instruction == "nop":
        revised_inputs[location] = "jmp %s" % (argument)
    else:
        continue
    result = run_program(revised_inputs)
    if result:
        break

print(result)