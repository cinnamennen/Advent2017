import pprint
import re
from tqdm import trange

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'x.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()

    return data


def get_binary(a):
    a_ = bin(a)[2:]
    # z = a_.zfill(16)
    return a_[-16:]


def main():
    data = get_input()
    print(data)


if __name__ == '__main__':
    main()
