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

def shift_contains(l):
    return l[0] >= l[2] and l[1] <= l[3] or l[0] <= l[2] and l[1] >= l[3] 
    
def shift_overlaps(l):
    a, b = (l[0], l[1]), (l[2], l[3])
    if a[0] > b[0]: 
        a, b = b, a
    return a[1] >= b[0]

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [[int(d) for d in re.findall(digit_re, line)] for line in file ]
        print(sum(shift_contains(line) for line in lines))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [[int(d) for d in re.findall(digit_re, line)] for line in file ]
        print(sum(shift_overlaps(line) for line in lines))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)