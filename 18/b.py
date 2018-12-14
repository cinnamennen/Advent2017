from multiprocessing import Queue, pool
import pprint
import queue

from collections import defaultdict
from typing import Tuple, List

from string import ascii_lowercase

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def run(data: List[str], i: int, registers: dict, inq, outq, sent):
    r = registers.copy()
    s = sent
    command, *args = data[i].split(' ')
    i += 1
    if command == 'snd':
        outq.put(get_register_or_value(args[0], r))
        # print("r{} pushing {}".format(r['p'], get_register_or_value(args[0], r)))
        s += 1
    elif command == 'set':
        r[args[0]] = get_register_or_value(args[1], r)
    elif command == 'add':
        r[args[0]] += get_register_or_value(args[1], r)
    elif command == 'mul':
        r[args[0]] *= get_register_or_value(args[1], r)
    elif command == 'mod':
        r[args[0]] %= get_register_or_value(args[1], r)
    elif command == 'rcv':
        # print("r{} retrieving".format(r['p']))
        r[args[0]] = inq.get(timeout=5)
    elif command == 'jgz':
        if get_register_or_value(args[0], r) > 0:
            i -= 1
            i += get_register_or_value(args[1], r)
    else:
        print("couldn't parse {} {}".format(command, args))

    return r, i, s


def get_register_or_value(param: str, registers: dict):
    return registers[param] if param in ascii_lowercase else int(param)


def get_input():
    data = process_input()
    return data


def simulate(p: int, instructions: List[str], i: Queue, o: Queue):
    sent = 0
    ic = 0

    registers = defaultdict(lambda: 0)
    registers['p'] = p
    while 0 <= ic < len(instructions):
        # print(registers['p'], end='')
        # print(i.get_nowait(), o.get_nowait())
        try:
            registers, ic, sent = run(instructions, ic, registers, i, o, sent)
        except queue.Empty:
            return sent


def main():
    data = get_input()

    p = pool.ThreadPool(processes=2)

    q0 = Queue()
    q1 = Queue()

    p.apply_async(simulate, (0, data, q0, q1))
    res1 = p.apply_async(simulate, (1, data, q1, q0))

    print(res1.get())


if __name__ == '__main__':
    main()
