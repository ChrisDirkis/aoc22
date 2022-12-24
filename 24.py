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

def d2v(d):
    match d:
        case (1, 0): return ">"
        case (-1, 0): return "<"
        case (0, 1): return "v"
        case (0, -1): return "^"

def v2d(v):
    match v:
        case "v": return (0, 1)
        case "^": return (0, -1)
        case ">": return (1, 0)
        case "<": return (-1, 0)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [line.strip() for line in file]
        grid = {}
        for j, line in enumerate(lines):
            for i, char in enumerate(line):
                grid[(i, j)] = char

        dims = (len(lines[0]), len(lines))

        bvs = [(v, grid[v]) for v in grid if grid[v] != "." and grid[v] != "#"]
        spaces = set(v for v in grid if grid[v] != "#")

        blizzards = [(v, v2d(d)) for v, d in bvs]

        def step(blizzards):
            new_blizzards = []
            for v, d in blizzards:
                n = add_t(v, d)
                if n[0] == dims[0] - 1:
                    n = (1, n[1])
                if n[1] == dims[1] - 1:
                    n = (n[0], 1)
                if n[0] == 0:
                    n = (dims[0] - 2, n[1])
                if n[1] == 0:
                    n = (n[0], dims[1] - 2)
                
                new_blizzards.append((n, d))
            return new_blizzards

        print("generating blizzard sets")

        allbs = [set()]
        for i in range(1000):
            blizzards = step(blizzards)

            allbs.append(set(v for v, d in blizzards))

        print("starting search")

        start = (1, 0)
        end = (dims[0] - 2, dims[1] - 1)

        max_steps_seen = 0

        def nei(v):
            nonlocal max_steps_seen
            me, steps = v

            if max_steps_seen < steps:
                #print(steps)
                max_steps_seen = steps

            blizz = allbs[steps + 1]
            for d in dirs:
                n = (me[0] + d[0], me[1] + d[1])
                if n not in spaces: continue
                if n in blizz: continue
                yield (n, steps + 1)

        def heu(v):
            return abs(v[0][0] - end[0]) + abs(v[0][1] - end[1]) 

        print(start, end)
        path = list(astar((start, 0), lambda x: x[0] == end, None, nei, 0, heu))
        last_step = path[-1][1]
        print("s2e", last_step)


def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [line.strip() for line in file]
        grid = {}
        for j, line in enumerate(lines):
            for i, char in enumerate(line):
                grid[(i, j)] = char

        dims = (len(lines[0]), len(lines))

        bvs = [(v, grid[v]) for v in grid if grid[v] != "." and grid[v] != "#"]
        spaces = set(v for v in grid if grid[v] != "#")

        blizzards = [(v, v2d(d)) for v, d in bvs]

        def step(blizzards):
            new_blizzards = []
            for v, d in blizzards:
                n = add_t(v, d)
                if n[0] == dims[0] - 1:
                    n = (1, n[1])
                if n[1] == dims[1] - 1:
                    n = (n[0], 1)
                if n[0] == 0:
                    n = (dims[0] - 2, n[1])
                if n[1] == 0:
                    n = (n[0], dims[1] - 2)
                
                new_blizzards.append((n, d))
            return new_blizzards

        print("generating blizzard sets")
        
        allbs = [set()]
        for i in range(1000):
            blizzards = step(blizzards)

            allbs.append(set(v for v, d in blizzards))

        print("starting search")

        start = (1, 0)
        end = (dims[0] - 2, dims[1] - 1)

        max_steps_seen = 0

        def nei(v):
            nonlocal max_steps_seen
            me, steps = v

            if max_steps_seen < steps:
                #print(steps)
                max_steps_seen = steps

            blizz = allbs[steps + 1]
            for d in dirs:
                n = (me[0] + d[0], me[1] + d[1])
                if n not in spaces: continue
                if n in blizz: continue
                yield (n, steps + 1)

        def heu(v):
            return abs(v[0][0] - end[0]) + abs(v[0][1] - end[1]) 
        def heu2(v):
            return abs(v[0][0] - start[0]) + abs(v[0][1] - start[1]) 

        print(start, end)
        path = list(astar((start, 0), lambda x: x[0] == end, None, nei, 0, heu))
        last_step = path[-1][1]
        print("s2e", last_step)
        path2 = list(astar((end, last_step), lambda x: x[0] == start, None, nei, 0, heu2))
        last_step_2 = path2[-1][1]
        print("e2s", last_step_2)
        path3 = list(astar((start, last_step_2), lambda x: x[0] == end, None, nei, 0, heu))
        last_step_3 = path3[-1][1]
        print("s2e2", last_step_3)
        print(last_step_3)


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)