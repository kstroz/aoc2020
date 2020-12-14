import math

file = open("input", "r")
lines = [line.strip() for line in file.readlines()]

PLANE_COLUMNS = 8
PLANE_ROWS = 128


def get_col(code):
    code = code[7:]
    left, right = (1, PLANE_COLUMNS)
    for letter in code:
        if letter == "L":
            right = math.floor((left + right) / 2)
        else:
            left = math.ceil((left + right) / 2)

    return left


def get_row(code):
    code = code[:7]
    front, bottom = (1, PLANE_ROWS)
    for letter in code:
        if letter == "F":
            bottom = math.floor((front + bottom) / 2)
        else:
            front = math.ceil((front + bottom) / 2)

    return front


def get_cords(code):
    return (get_row(code), get_col(code))


def get_id(cords):
    row, col = cords
    return (row - 1) * 8 + (col - 1)


seats_ids = [get_id(get_cords(line)) for line in lines]
print(max(seats_ids))

seats_ids.sort()
seats_ids = seats_ids[1:-1]
counter = min(seats_ids)

for id in seats_ids:
    if id != counter:
        print(id)
        break
    counter += 1
