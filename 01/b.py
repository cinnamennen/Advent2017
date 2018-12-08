file = 'a.txt'
data = [_.strip() for _ in open(file).readlines()]


def clean(input: str):
    output = []
    for index in range(len(input)):
        if input[index] == input[index-(len(input)//2)]:
            output.append(int(input[index]))

    return sum(output)


print([clean(x) for x in data])
