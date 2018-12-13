from collections import deque
from functools import reduce


def formatting(data):
    data = [ord(d) for d in data]
    data += [17, 31, 73, 47, 23]
    return data


def r(p, ss, k, data):
    for length in data:
        a = [k.popleft() for _ in range(length)]
        for g in a:
            (k.appendleft(g))

        k.rotate(-1 * (length + ss))
        p += (length + ss)
        ss += 1
    return p, ss, k


def kh(i):
    d = formatting(i)

    knot = deque(range(256))

    position = 0
    skip_size = 0
    for _ in range(64):
        position, skip_size, knot = r(position, skip_size, knot, d)
    knot.rotate(position)
    temp = [reduce(lambda a, b: a ^ b, [knot.popleft() for _ in range(16)]) for __ in range(16)]
    temp = [hex(d)[2:].zfill(2) for d in temp]
    # print(temp)
    temp = "".join(temp)
    return (temp)
