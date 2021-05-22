import string
from random import choices
import argparse


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
    parser = argparse.ArgumentParser(
        description='this is a password generator with positional and optional argument'
    )
    parser.add_argument('length', type=int, help='length of password!')
    parser.add_argument('-U', '--upper', help='upper case', action='store_true')
    parser.add_argument('-L', '--lower', help='lower case', action='store_true')
    parser.add_argument('-P', '--punc', help='punctuation for password!', action='store_true')
    parser.add_argument('-D', '--digits', help='digits for password!', action='store_true')

    args = parser.parse_args()
    print(args)
    print(pass_generator(args.length, args.upper, args.lower, args.punc, args.digits))
