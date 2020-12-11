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
            merged[i] = merged[i] + text

    return merged


def is_valid(element):
    matches = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    return all(match in element for match in matches)


print(len(list(filter(is_valid, passport_cleaner(lines)))))
