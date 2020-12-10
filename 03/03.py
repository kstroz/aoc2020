from functools import reduce

file = open("input", "r")
slope = [line.strip() for line in file.readlines()]
cords = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]


def tree_counter(movement):
    counter = 0
    col_mov, row_mov = movement
    col, row = (0, 0)
    row_len = len(slope[0])

    while row < len(slope):
        if slope[row][col] == "#":
            counter += 1

        if col + col_mov >= row_len:
            col = col_mov - (row_len - col)
        else:
            col += col_mov

        row += row_mov

    return counter


# Part 1
print(f"Part 1: {tree_counter((3, 1))}")


# Part 2
print(f"Part 2: {reduce((lambda n1, n2: n1 * n2), map(tree_counter, cords))}")
