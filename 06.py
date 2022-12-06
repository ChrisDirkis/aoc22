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
        buffer = file.read()
        for n, (i, j, k, l) in enumerate(zip(buffer, buffer[1:], buffer[2:], buffer[3:])):
            print(i, j, k, l)
            if len(set([i, j, k, l])) == 4:
                print(n + 4)
                return

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        buffer = file.read()
        for n, chars in enumerate(zip(*[buffer[n:] for n in range(14)])):
            if len(set(chars)) == len(chars):
                print(n + 14)
                return


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)