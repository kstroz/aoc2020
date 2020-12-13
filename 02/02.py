file = open("input", "r")
passwords = [password for password in file.readlines()]


def old_password_validator(password):
    range_of, letter, password = password.split()
    n1, n2 = map(int, range_of.split("-"))
    range_of = range(n1, n2 + 1)
    return password.count(letter[0], 0, len(password)) in range_of


def new_password_validator(password):
    range_of, letter, password = password.split()
    letter = letter[0]
    n1, n2 = map(int, range_of.split("-"))
    answers = (password[n1 - 1] == letter, password[n2 - 1] == letter)

    return len(set(answers)) == 2


print(len(list(filter(old_password_validator, passwords))))
print(len(list(filter(new_password_validator, passwords))))
