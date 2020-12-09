file = open("input", "r")
passwords = [password for password in file.readlines()]


def password_validator(password):
    range_of, letter, password = password.split()
    n1, n2 = map(int, range_of.split("-"))
    range_of = range(n1, n2 + 1)
    return password.count(letter[0], 0, len(password)) in range_of


print(len(list(filter(password_validator, passwords))))
