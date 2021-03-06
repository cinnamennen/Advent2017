import pprint
import re

from collections import deque
from tqdm import trange, tqdm

from string import ascii_lowercase

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def spin(d: deque, amount: int):
    d.rotate(amount)


def exchange(d: deque, a: int, b: int):
    d[a], d[b] = d[b], d[a]


def partner(d: deque, x: str, y: str):
    a, b = d.index(x), d.index(y)
    exchange(d, a, b)



def get_input():
    data = process_input()[0]
    data = data.split(',')

    return data


def main():
    data = get_input()
    d = deque(ascii_lowercase[:16])

    for instruction in tqdm(data):
        op, a = instruction[0], instruction[1:].split('/')
        if op == 's':
            spin(d, int(instruction[1:]))
        elif op == 'x':
            exchange(d, *map(int, a))
        elif op == 'p':
            partner(d, *a)
        else:
            print("Could not process {}".format(instruction))

    print("".join(d))


if __name__ == '__main__':
    main()
