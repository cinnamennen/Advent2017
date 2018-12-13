import itertools
import pprint
import re
from hashing import kh
import binascii

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    data = data[0]

    return data


def main():
    data = get_input()
    hashes = [kh("{}-{}".format(data, n)) for n in range(128)]
    # print(hashes)
    hashes = [bin(int(h, 16))[2:].zfill(128) for h in hashes]
    hashes = [h.count('1') for h in hashes]
    hashes = sum(hashes)
    print(hashes)


if __name__ == '__main__':
    main()
