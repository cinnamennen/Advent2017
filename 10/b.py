import pprint
from collections import deque
from functools import reduce

pp = pprint.PrettyPrinter(indent=4)

file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]
data = [list(d) for d in data][0]
data = [ord(d) for d in data]
data += [17, 31, 73, 47, 23]

# print(data)
knot = deque(range(256))

position = 0
skip_size = 0


def round():
    global position, skip_size, knot
    for length in data:
        a = [knot.popleft() for _ in range(length)]
        for g in a:
            (knot.appendleft(g))

        knot.rotate(-1 * (length + skip_size))
        position += (length + skip_size)
        skip_size += 1


for _ in range(64):
    round()

knot.rotate(position)

temp = [reduce(lambda a, b: a ^ b, [knot.popleft() for _ in range(16)]) for __ in range(16)]
temp = [hex(d)[2:].zfill(2) for d in temp]
# print(temp)
temp = "".join(temp)
print(temp)

