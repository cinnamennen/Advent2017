import pprint

pp = pprint.PrettyPrinter(indent=4)
file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]
data = [["".join(sorted(list(k))) for k in d.split()] for d in data]

data = [(sorted(list(set(d))) == sorted(d)) for d in data]
data = data.count(True)
pp.pprint(data)
