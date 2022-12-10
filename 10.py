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

def get_acc(lines):
    cycs = []
    x = 1
    cycs.append(x)
    for line in lines:
        if line.startswith("noop"):
            cycs.append(x)
            continue
        if line.startswith("addx"):
            cycs.append(x)
            cycs.append(x)
            x += int(line.split(" ")[1])
            continue
    cycs.append(x)
    return cycs

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [line.strip() for line in file]
        times = [20, 60, 100, 140, 180, 220]
        accs = get_acc(lines)
        print(accs)
        print(sum(accs[time] * time for time in times))

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [line.strip() for line in file]
        accs = get_acc(lines)
        width = 40
        height = 6
        out = gen_grid((width, height), " ")
        for i in range(width * height):
            x = i % width
            y = i // width
            acc = accs[i] + 1
            if acc - 1 <= x <= acc + 1:
                out[(x, y)] = "#"
        print_grid(out, (width, height))

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)