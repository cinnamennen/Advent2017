import pprint
from collections import deque

pp = pprint.PrettyPrinter(indent=4)

file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]
data = [d.split(',') for d in data][0]
data = [int(d) for d in data]

knot = deque(range(256))


position = 0
skip_size = 0
for length in data:
    a = [knot.popleft() for _ in range(length)]
    for g in a:
        (knot.appendleft(g))

    knot.rotate(-1 * (length + skip_size))
    position += (length + skip_size)
    skip_size += 1

knot.rotate(position)
# print(knot)

print(knot[0] * knot[1])
