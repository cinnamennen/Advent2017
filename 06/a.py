import pprint
from typing import List

pp = pprint.PrettyPrinter(indent=4)
file = 'a.txt'
data = [list(map(int, _.strip().split())) for _ in open(file).readlines()][0]

seen = set()


def remember(layout: List[int]):
    conversion = "".join(map(str, layout))
    if conversion not in seen:
        seen.add(conversion)
        return False
    else:
        return True


def redistribute():
    memory = data
    bank = memory.index(max(memory))

    blocks = memory[bank]
    memory[bank] = 0

    pos = bank
    pos += 1
    pos %= len(memory)
    while blocks > 0:
        memory[pos] += 1
        blocks -= 1

        pos += 1
        pos %= len(memory)

    return memory


count = 1
while not remember(redistribute()):
    count += 1
print(count)
