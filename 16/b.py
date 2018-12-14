import pprint

from collections import deque
from tqdm import trange

from string import ascii_lowercase
from helpers import memoized

pp = pprint.PrettyPrinter(indent=4)

ops = None

class MyDeque(deque):
    def __hash__(self):
        return hash(str(self))
    def __str__(self):
        return "".join(self)

def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def spin(d: MyDeque, amount: int):
    d.rotate(amount)


def exchange(d: MyDeque, a: int, b: int):
    d[a], d[b] = d[b], d[a]


def partner(d: MyDeque, x: str, y: str):
    a, b = d.index(x), d.index(y)
    exchange(d, a, b)



def get_input():
    data = process_input()[0]
    data = data.split(',')

    return data


def main():
    global ops
    data = get_input()
    ops = data
    d = MyDeque(ascii_lowercase[:16])
    d = str(d)

    for _ in trange(1000000000):
        d = run_round(d)

    print(d)

@memoized
def run_round(in_d: str):
    # print("running on", in_d)
    global ops
    d = MyDeque(list(in_d))
    for instruction in ops:
        op, a = instruction[0], instruction[1:].split('/')
        if op == 's':
            spin(d, int(instruction[1:]))
        elif op == 'x':
            exchange(d, *map(int, a))
        elif op == 'p':
            partner(d, *a)
        else:
            print("Could not process {}".format(instruction))
    # print("sending back", s)
    return str(d)


if __name__ == '__main__':
    main()
