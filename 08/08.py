file = open("input", "r")
lines = [line.strip() for line in file.readlines()]


def accumulator(instructions):
    acc = 0
    indexes = []
    current_index = 0
    instructions = list(enumerate(instructions))

    while current_index not in indexes:
        indexes.append(current_index)

        current_index, instruction = instructions[current_index]
        cmd, val = instruction.split()
        val = int(val.replace("+", ""))

        if cmd == "nop":
            current_index += 1
        elif cmd == "acc":
            current_index += 1
            acc += val
        else:
            current_index += val

    return acc


print(accumulator(lines))
