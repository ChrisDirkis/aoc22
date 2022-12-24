from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict, deque

from grid import *

digit_re = re.compile(r"(-?\d+)")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [[int(d) for d in digit_re.findall(line)] for line in file]
        lava = [vec3(*line) for line in lines]

        print(sum(sum(a not in lava for a in adj4(v)) for v in lava))

        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:        
        lines = [[int(d) for d in digit_re.findall(line)] for line in file]
        lava = set(vec3(*line) for line in lines)

        mi, ma = minmax_grid(lava)
        mi = sub_t(mi, vec3(1, 1, 1))
        ma = add_t(ma, vec3(1, 1, 1))

        frontier = deque()
        frontier.append(mi)
        steam = set()

        while frontier:
            v = frontier.popleft()
            for a in adj4(v):
                if a in steam: continue
                if a in lava: continue
            
                if lt_t(a, mi): continue
                if gt_t(a, ma): continue

                steam.add(a)
                frontier.append(a)

        print(sum(sum(a in steam and a not in lava for a in adj4(v)) for v in lava))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)