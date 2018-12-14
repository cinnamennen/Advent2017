import pprint
import re

from collections import deque
from tqdm import trange

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = int(process_input()[0])

    return data

def main():
    data = get_input()

    d = deque([0])
    for i in range(1,2018):
        d.rotate(-data)
        d.append(i)
    pp.pprint(d[0])


if __name__ == '__main__':
    main()
