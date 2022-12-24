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

        vecs = [vec3(*line) for line in lines]

        s = 0
        for vec in vecs:
            for a in adj4(vec):
                if a not in vecs:
                    s += 1
        print(s)
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:        
        lines = [[int(d) for d in digit_re.findall(line)] for line in file]
        lava = set(vec3(*line) for line in lines)

        min_x = min(lava, key=lambda v: v.x).x
        min_y = min(lava, key=lambda v: v.y).y
        min_z = min(lava, key=lambda v: v.z).z
        max_x = max(lava, key=lambda v: v.x).x
        max_y = max(lava, key=lambda v: v.y).y
        max_z = max(lava, key=lambda v: v.z).z

        mi = vec3(min_x - 1, min_y - 1, min_z - 1)
        ma = vec3(max_x + 1, max_y + 1, max_z + 1)
        frontier = deque()
        frontier.append(mi)
        steam = set()

        while frontier:
            v = frontier.popleft()
            for a in adj4(v):
                if a in steam: continue
                if a in lava: continue
            
                if any(ca < cb for ca, cb in zip(a, mi)): continue
                if any(ca > cb for ca, cb in zip(a, ma)): continue

                steam.add(a)
                frontier.append(a)

        s = 0
        for vec in lava:
            for a in adj4(vec):
                if a not in lava and a in steam:
                    s += 1
        print(s)


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)