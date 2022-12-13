import functools
from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from grid import *

digit_re = re.compile(r"(\d+)")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"


def cmp(a, b):
    
    if isinstance(a, int) and isinstance(b, int):
        return b - a

    for i, v in enumerate(a):
        if i >= len(b):
            return -1

        ai = a[i]
        bi = b[i]
        if isinstance(ai, int) and not isinstance(bi, int):
            ai = [ai]
        elif isinstance(bi, int) and not isinstance(ai, int):
            bi = [bi]

        c = cmp(ai, bi)
        if c != 0:
            return c

    return 1 if len(b) > len(a) else 0

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        pairs = [[eval(pe) for pe in p.splitlines()] for p in file.read().split("\n\n")]
        
        print([i for i, pair in enumerate(pairs) if cmp(*pair) >= 0])
        print(sum(i + 1 for i, pair in enumerate(pairs) if cmp(*pair) >= 0))
            
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        pairs = [[eval(pe) for pe in p.splitlines()] for p in file.read().split("\n\n")]
        flat = [item for sublist in pairs for item in sublist]
        two = [[2]]
        six = [[6]]
        flat.append(two)
        flat.append(six)
        flat.sort(key=functools.cmp_to_key(cmp))
        flat = list(reversed(flat))
        print((flat.index(two) + 1) * (flat.index(six) + 1))

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)