file = open("input", "r")
lines = [int(num) for num in file.readlines()]


def find_sum_from_two(sum, numbers):
    numbers = numbers.copy()

    for index, n1 in enumerate(numbers):
        for n2 in numbers:
            if n1 + n2 == 2020:
                return n1 * n2

        numbers.pop(index)


def find_sum_from_three(sum, numbers):
    numbers = numbers.copy()

    for index, n1 in enumerate(numbers):
        for n2 in numbers:
            for n3 in numbers:
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3

        numbers.pop(index)


print(find_sum_from_two(2020, lines))
print(find_sum_from_three(2020, lines))
