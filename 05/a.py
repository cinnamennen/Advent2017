import pprint


def d_print(pos: int, d: list, step=''):
    before, at, after = d[:pos], str(d[pos]), d[pos + 1:]
    b = ' ' + "  ".join(map(str, before))
    if b == ' ':
        b = ''
    else:
        b += ' '
    at_ = "(" + at + ") "
    a = "  ".join(map(str, after))
    print(step, b + at_ + a)


pp = pprint.PrettyPrinter(indent=4)
file = 'a.txt'
data = [int(_.strip()) for _ in open(file).readlines()]
# pp.pprint(data)


position = 0
steps = 0

while 0 <= position < len(data):
    data[position], position, steps = (data[position]+1), position + data[position], steps + 1


print(steps)
