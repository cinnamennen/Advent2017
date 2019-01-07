import pprint
import re
from tqdm import trange
import numpy as np

pp = pprint.PrettyPrinter(indent=4)


def rotate(matrix):
    return zip(*matrix[::-1])


def process_input():
    file = 'a.txt'
    data = [_.strip() for _ in open(file).readlines()]
    return data


def get_input():
    replacements = {}
    data = process_input()
    for d in data:
        original, v = list(map(translate_to_np, d.split(' => ')))
        flip = np.fliplr(original)

        for i in range(4):
            replacements[original.tobytes()] = v
            replacements[flip.tobytes()] = v
            original, flip = np.rot90(original), np.rot90(flip)
    # print(data)
    # print(replacements)

    return replacements


def translate_to_np(s):
    # return np.array([[c == '#' for c in l]
    #                  for l in s.split('/')])
    return np.array([[c for c in l]
                     for l in s.split('/')])


def split(array, sub_size):
    """Split a matrix into sub-matrices."""

    r, h = array.shape
    return (array.reshape(h // sub_size, sub_size, -1, sub_size)
            .swapaxes(1, 2)
            .reshape(-1, sub_size, sub_size))


def enhance(picture, r):
    resolution = 2 if len(picture[0]) % 2 == 0 else 3
    # print(picture_resolution)
    shape = split(picture, resolution)
    # print(shape)
    s, *x = shape.shape
    i = int(np.sqrt(s))

    # i = len(shape) // resolution
    # s = [i, i] + x
    # print(s)
    shape = np.reshape(shape, [i]*2+ x)
    # print(shape)
    shape = np.array([[r[col.tobytes()] for col in row] for row in shape])
    a,b,c,d = shape.shape
    # shape = shape.flatten()
    # shape = np.reshape(shape, (a*c, b*d, 1, 1))
    # print(shape)
    shape = np.array(np.concatenate([np.concatenate([col for col in row], axis=1) for row in shape]))
    # print(shape)

    return shape


def main():
    r = get_input()
    # pp.pprint(r)
    # exit()
    # start = "##.##./#..#../....../##.##./#..#../......"
    start = ".#./..#/###"
    # start = "#..#/..../..../#..#"
    picture = translate_to_np(start)

    for _ in range(18):
        picture = enhance(picture, r)

    # print(picture)
    picture = picture.flatten()
    unique, counts = np.unique(picture, return_counts=True)
    print(dict(zip(unique, counts))['#'])


if __name__ == '__main__':
    main()
