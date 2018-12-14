import pprint
import re

from collections import defaultdict
from typing import Tuple, List

from tqdm import trange
from string import ascii_lowercase

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def run(data: List[str], i: int, registers: dict, last_played: int):
    r = registers.copy()
    l = last_played
    command, *args = data[i].split(' ')
    i += 1
    if command == 'snd':
        l = get_register_or_value(args[0], r)
        # print("played freq {}".format(l))
    elif command == 'set':
        r[args[0]] = get_register_or_value(args[1], r)
    elif command == 'add':
        r[args[0]] += get_register_or_value(args[1], r)
    elif command == 'mul':
        r[args[0]] *= get_register_or_value(args[1], r)
    elif command == 'mod':
        r[args[0]] %= get_register_or_value(args[1], r)
    elif command == 'rcv':
        if get_register_or_value(args[0], r) != 0:
            print("retrieved freq {}".format(l))
            # exit()
    elif command == 'jgz':
        if get_register_or_value(args[0], r) > 0:
            i -= 1
            i += get_register_or_value(args[1], r)
    else:
        print("couldn't parse {} {}".format(command, args))

    return r, l, i


def get_register_or_value(param: str, registers: dict):
    return registers[param] if param in ascii_lowercase else int(param)


def get_input():
    data = process_input()
    return data


def main():
    data = get_input()
    registers = defaultdict(lambda: 0)
    last_played = -1
    i = 0
    while 0 <= i < len(data):
        # print("running {}".format(data[i]))
        registers, last_played, i = run(data, i, registers, last_played)
        # pp.pprint(registers)
        # break


if __name__ == '__main__':
    main()
