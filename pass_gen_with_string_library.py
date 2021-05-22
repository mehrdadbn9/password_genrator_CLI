import string
from random import choices


def pass_generator(length=8, upper=False, lower=False, punc=False, digit=False):
    selected = ''

    if upper:
        selected += string.ascii_uppercase

    if lower:
        selected += string.ascii_lowercase

    if punc:
        selected += string.punctuation

    if digit:
        selected += string.digits

    if selected == '':
        selected = string.ascii_letters

    return ''.join(choices(selected, k=length))


if __name__ == "__main__":
    print(pass_generator(14, 1, 1, 0, 1))
