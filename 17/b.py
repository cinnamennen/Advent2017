import pprint
import re

from collections import deque
from tqdm import trange

pp = pprint.PrettyPrinter(indent=4)


data = 343

d = deque([0])
for i in trange(1, 50000001, mininterval=1, miniters=100):
    d.rotate(-data)
    d.append(i)
print(d[d.index(0) + 1])
