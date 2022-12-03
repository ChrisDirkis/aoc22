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

def value(c):
    if ord(c) >= ord("a"):
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [line.strip() for line in file]
        slines = [(line[:len(line)//2],line[len(line)//2:]) for line in lines]
        same = [[c for c in a if c in b] for a, b in slines]
        su = [c[0] for c in same]
        values = [value(c) for c in su]
        print(sum(values))

        pass

def part_2(filename):
    def divide_chunks(l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]
        pass
    
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [line.strip() for line in file]
        sets = list(divide_chunks(lines, 3))
        ssets = [[set(a) for a in l] for l in sets]
        badges = [next(iter(setg[0] & setg[1] & setg[2])) for setg in ssets]
        print(sum(value(b) for b in badges))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)