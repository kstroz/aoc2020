from functools import reduce

file = open("input", "r")
lines = [line.strip() for line in file.readlines()]


def merge_answers(answers):
    merged = [""]
    people_in_group = 0
    i = 0
    for a_i, answer in enumerate(answers):
        if answer == "":
            merged[i] = [people_in_group, merged[i]]
            merged.append("")
            i += 1
            people_in_group = 0
        else:
            people_in_group += 1
            merged[i] = merged[i] + answer

        if a_i + 1 == len(answers):
            merged[i] = [people_in_group, merged[i]]

    return merged


def count_all_group(group):
    counter = 0
    occured = []
    people_in_group = group[0]
    group_answers = group[1]

    for answer in group_answers:
        if answer not in occured:
            occured.append(answer)

            if people_in_group == group_answers.count(answer):
                counter += 1

    return counter


counted_any = [len(set(x[1])) for x in merge_answers(lines)]
print(reduce(lambda a, b: a + b, counted_any))
print(reduce(lambda a, b: a + b, map(count_all_group, merge_answers(lines))))
