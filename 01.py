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

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        data = file.read()
        groups = [group.split("\n") for group in data.split("\n\n")]
        sumg = [sum(int(line) for line in group) for group in groups]
        print(max(sumg))

        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        data = file.read()
        groups = [group.split("\n") for group in data.split("\n\n")]
        sumg = [sum(int(line) for line in group) for group in groups]
        print(sum(sorted(sumg)[-3:]))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)