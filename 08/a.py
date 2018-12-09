import pprint
import re
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]
data = [re.search(r"(\w) (\w*) (-?\d*) if (\w*) (.*) (-?\d*)", d).groups() for d in data]

registers = defaultdict(lambda: 0)


def test(a, op, b):
    if op == '==':
        return a == b
    if op == '!=':
        return a != b
    if op == '>':
        return a > b
    if op == '<':
        return a < b
    if op == '<=':
        return a <= b
    if op == '>=':
        return a >= b
    raise ValueError


def calculate(a, op, b):
    if op == 'inc':
        return a + b
    if op == 'dec':
        return a - b


for register, op, amount, check, comparison, value in data:
    print(f"{check} {comparison} {value} is {registers[check]} {comparison} {int(value)} which is ", end="")
    if test(registers[check], comparison, int(value)):
        print("true")
        registers[register] = calculate(registers[register], op, int(amount))
    else:
        print("false")
print(max(registers.values()))
pp.pprint(registers)