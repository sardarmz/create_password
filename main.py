import argparse
import string
import random


def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    context = ''

    if upper:
        context += string.ascii_uppercase
    if lower:
        context += string.ascii_lowercase
    if digit:
        context += string.digits
    if pun:
        context += string.punctuation

    if context == '':
        context += string.ascii_letters

    return ''.join(random.choices(context, k=length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='create context')
    
    parser.add_argument('length', type=int, help='add upper')
    parser.add_argument('-u', '--upper', help='add upper', action='store_true')
    parser.add_argument('-l', '--lower', help='add lower', action='store_true')
    parser.add_argument('-d', '--digit', help='add digit', action='store_true')
    parser.add_argument('-p', '--pun', help='add pun', action='store_true')
    
    args = parser.parse_args()
    password = create_password(args.length, args.upper, args.lower, args.digit, args.pun)
    print(password)
