from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from grid import *

digit_re = re.compile(r"(-?\d+)")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"

def rot_ccw(v): return vec2(v.y, -v.x)
def rot_cw(v): return vec2(-v.y, v.x)

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        [a, b] = file.read().split("\n\n")

        a = a.split("\n")
        grid = {}
        for j, line in enumerate(a):
            for i, c in enumerate(line):
                if c == "\n": continue
                if c == " ": continue
                v = vec2(i + 1, j +  1)
                grid[v] = c

        def step(point, dir):

            next = add_t(point, dir)

            if next not in grid:
                next = point
                while next in grid:
                    next = sub_t(next, dir)
                next = add_t(next, dir)

            if grid[next] == "#": return point
            return next

        steps = re.findall("(\d+)([RL])", b)

        loc = vec2(a[0].index(".") + 1, 1)
        dir = vec2(1, 0)

        print(loc, dir, loc in grid)
        for dist, rot in steps:
            for _ in range(int(dist)):
                loc = step(loc, dir)
                grid[loc] = "X"
            if rot == "R":
                dir = rot_cw(dir)
            else:
                dir = rot_ccw(dir)
            
            #print(loc, dir)

        
        match dir:
            case vec2(1, 0): f = 0
            case vec2(0, 1): f = 1
            case vec2(-1, 0): f = 2
            case vec2(0, -1): f = 3
        print(loc, dir, f)
        print(loc.y * 1000 + loc.x * 4 + f)
        
            


        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        [a, b] = file.read().split("\n\n")

        a = a.split("\n")

        grid = {}
        for j, line in enumerate(a):
            for i, c in enumerate(line):
                if c == "\n": continue
                if c == " ": continue
                v = vec2(i + 1, j +  1)
                grid[v] = c

        teleports = {}
        w = 50

        # 2 and 3
        for v in range(w):
            p = vec2(101 + v, 50)
            q = vec2(100, 51 + v)
            teleports[(p, vec2(0, 1))] = (q, vec2(-1, 0), (2, 3))
            teleports[(q, vec2(1, 0))] = (p, vec2(0, -1), (3, 2))

        # 4 and 6
        for v in range(w):
            p = vec2(51 + v, 150)
            q = vec2(50, 151 + v)
            teleports[(p, vec2(0, 1))] = (q, vec2(-1, 0), (4, 6))
            teleports[(q, vec2(1, 0))] = (p, vec2(0, -1), (6, 4))

        # 2 and 4
        for v in range(w):
            p = vec2(150, 1 + v)
            q = vec2(100, 150 - v)
            teleports[(p, vec2(1, 0))] = (q, vec2(-1, 0), (2, 4))
            teleports[(q, vec2(1, 0))] = (p, vec2(-1, 0), (4, 2))

        # 2 and 6
        for v in range(w):
            p = vec2(101 + v, 1)
            q = vec2(1 + v, 200)
            teleports[(p, vec2(0, -1))] = (q, vec2(0, -1), (2, 6))
            teleports[(q, vec2(0, 1))] = (p, vec2(0, 1), (6, 2))

        # 1 and 6
        for v in range(w):
            p = vec2(51 + v, 1)
            q = vec2(1, 151 + v)
            teleports[(p, vec2(0, -1))] = (q, vec2(1, 0), (1, 6))
            teleports[(q, vec2(-1, 0))] = (p, vec2(0, 1) ,(6, 1))

        # 1 and 5
        for v in range(w):
            p = vec2(51, 1 + v)
            q = vec2(1, 150 - v)
            teleports[(p, vec2(-1, 0))] = (q, vec2(1, 0), (1, 5))
            teleports[(q, vec2(-1, 0))] = (p, vec2(1, 0), (5, 1))

        # 5 and 3
        for v in range(w):
            p = vec2(51, 51 + v)
            q = vec2(1 + v, 101)
            teleports[(p, vec2(-1, 0))] = (q, vec2(0, 1), (3, 5))
            teleports[(q, vec2(0, -1))] = (p, vec2(1, 0), (5, 3))

        def step(point, dir):

            if (point, dir) in teleports:
                next, nd, ft = teleports[(point, dir)]
                pass
            else:
                next, nd = add_t(point, dir), dir

            if grid[next] == "#": return (point, dir)

            return next, nd

        steps = re.findall("(\d+)([RL]?)", b)

        loc = vec2(a[0].index(".") + 1, 1)
        dir = vec2(1, 0)

        print(loc, dir, loc in grid)
        for dist, rot in steps:
            for _ in range(int(dist)):
                loc, dir = step(loc, dir)
                grid[loc] = "X"
            if rot == "R":
                dir = rot_cw(dir)
            elif rot == "L":
                dir = rot_ccw(dir)

            print(loc, dir)
        
        match dir:
            case vec2(1, 0): f = 0
            case vec2(0, 1): f = 1
            case vec2(-1, 0): f = 2
            case vec2(0, -1): f = 3
        print(loc, dir, f)
        print(loc.y * 1000 + loc.x * 4 + f)

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    #part_2(testing_file_name, 4)
    part_2(data_file_name)