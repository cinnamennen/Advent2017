file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]

data = [list(map(int, _.split())) for _ in data]

data = [max(row) - min(row) for row in data]

data = sum(data)

print(data)
