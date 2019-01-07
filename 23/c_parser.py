data = [_.strip().split() for _ in open('a.txt').readlines()]

i = -1


def clean(x):
    global i
    i += 1
    rv = 'line' + str(i) + ': '
    if x[0] == 'set':
        rv += x[1] + ' = ' + x[2]
    elif x[0] == 'sub':
        rv += x[1] + ' -= ' + x[2]
    elif x[0] == 'mul':
        rv += x[1] + ' *= ' + x[2]
    else:
        rv += 'if (' + x[1] + ') { j = ' + str(i + int(x[2])) + '; goto jump;}'
    return rv + ';'


data = [clean(d) for d in data]
print('\n'.join(data))
