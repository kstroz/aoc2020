import re

file = open("input", "r")
lines = [line.strip() for line in file.readlines()]


def passport_cleaner(passports):
    merged = [""]
    i = 0
    for text in lines:
        if text == "":
            merged.append("")
            i += 1
        else:
            merged[i] = f"{merged[i]} {text}"

    return merged


def is_valid(element, strict_policy):
    matches = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    strict_matches = [
        "byr:(19[2-9][0-9]|200[0-2])",
        "iyr:20(1[0-9]|20)",
        "eyr:20(2[0-9]|30)",
        "hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)",
        "hcl:#[a-f0-9]{6}",
        "ecl:(amb|blu|brn|gry|grn|hzl|oth)",
        "pid:\d{9}",
    ]
    strict_matches = [x + "(\s|$)" for x in strict_matches]
    policy = strict_matches if strict_policy else matches

    return all(bool(re.search(match, element)) for match in policy)


print(len(list(filter(lambda i: is_valid(i, False), passport_cleaner(lines)))))
print(len(list(filter(lambda i: is_valid(i, True), passport_cleaner(lines)))))
