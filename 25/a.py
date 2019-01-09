import pprint
import re
from collections import defaultdict

from tqdm import trange

pp = pprint.PrettyPrinter(indent=4)


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    data = process_input()
    begin = data.pop(0)[-2]
    steps = int(re.findall(r'\d+', data.pop(0))[0])
    data.pop(0)
    data = '\n'.join(data)
    data = re.findall(r" (\w+)(?::|\.)", data)
    data = [data[i:i + 9] for i in range(0, len(data), 9)]
    # print(data)
    # print(data)
    data = {state: {int(v1): (int(w1), -1 if d1 == 'left' else 1, c1),
                    int(v2): (int(w2), -1 if d2 == 'left' else 1, c2)
                    } for state, v1, w1, d1, c1, v2, w2, d2, c2 in data}
    return begin, steps, data


def main():
    instruction, steps, commands = get_input()
    turing = defaultdict(lambda: 0)
    position = 0
    # print(instruction, steps)
    # pp.pprint(commands)

    for _ in trange(steps):
        write, move, step = commands[instruction][turing[position]]
        # print(write, move, step)
        turing[position] = write
        position += move
        instruction = step
        # for __ in range(-3, 3):
        #     print('[' + str(turing[__]) + ']' if __ == position else ' ' + str(turing[__]) + ' ', end='')
        # print("after ", str(_), " steps; about to run state ", str(instruction), ' position ', position)
    print(list(turing.values()).count(1))



if __name__ == '__main__':
    main()
