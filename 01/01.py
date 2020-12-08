file = open("input", "r")
lines = [int(num) for num in file.readlines()]


def find_sum(sum, numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j


print(find_sum(2020, lines))
