from functools import reduce

file = open("input", "r")
lines = [line.strip() for line in file.readlines()]


def merge_answers(answers):
    merged = [""]
    i = 0
    for answer in answers:
        if answer == "":
            merged.append("")
            i += 1
        else:
            merged[i] = merged[i] + answer

    return merged


counted_answers = [len(set(x)) for x in merge_answers(lines)]
print(reduce(lambda a, b: a + b, counted_answers))
