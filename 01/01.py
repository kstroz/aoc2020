file = open("input", "r")
lines = [int(num) for num in file.readlines()]


def find_sum(sum, numbers):
    for index, i in enumerate(numbers):
        for j in numbers:
            if i + j == 2020:
                return i * j

        numbers.pop(index)


print(find_sum(2020, lines))
