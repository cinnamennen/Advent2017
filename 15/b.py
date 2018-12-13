import pprint
import re

from tqdm import trange

from helpers import memoized

pp = pprint.PrettyPrinter(indent=4)

a_factor = 16807
b_factor = 48271
divisor = 2147483647


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    data = [int(re.findall(r'\d+', d)[0]) for d in data]

    return data


def generate(previous, factor):
    rv = previous
    rv *= factor
    rv %= divisor
    return rv


# @memoized
def next_a(previous):
    return generate(previous, a_factor)


# @memoized
def next_b(previous):
    return generate(previous, b_factor)

# @memoized
def binary_match(a: int, b: int) -> bool:
    bin_a = get_binary(a)
    bin_b = get_binary(b)
    return bin_a == bin_b


def get_binary(a):
    a_ = bin(a)[2:]
    # z = a_.zfill(16)
    return a_[-16:]


def main():
    data = get_input()
    a, b = data
    match = 0
    for _ in trange(int(4E7)):
        a = next_a(a)
        b = next_b(b)
        if binary_match(a, b):
            match += 1
    print("\n\n\n",match)


if __name__ == '__main__':
    main()
