import pprint
import re

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    data = [list(map(int, d.split(': '))) for d in data]

    return {p: h for p, h in data}


def get_firewall_position(height: int, time: int):
    offset = time % ((height - 1) * 2)
    return 2 * (height - 1) - offset if offset > height - 1 else offset


def main():
    data = get_input()
    print(sum(pos * data[pos] for pos in data if get_firewall_position(data[pos], pos) == 0)
)


if __name__ == '__main__':
    main()
