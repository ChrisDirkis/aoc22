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
        lines = [[int(d) for d in digit_re.findall(line)] for line in file]
        groups = [list(vec2(x, y) for [x, y] in chunk(l, 2)) for l in lines]
        
        grid = {vec2(500, 0): "v"}
        for group in groups:
            for a, b in zip(group, group[1:]):
                for point in aaline(a, b):
                    grid[point] = "#"
                    #print(point)

        lowest_y = max(p.y for p in grid)

        for i in count():
            p = vec2(500, 0)

            while True:
                if p.y > lowest_y:
                    print_grid(grid, (40, 20), (480, 0), width=1, separator="")
                    print(i)
                    return

                south = add_t(p, vec2(0, 1))
                if not south in grid:
                    p = south
                    continue
                se = add_t(p, vec2(-1, 1))
                if not se in grid:
                    p = se
                    continue
                sw = add_t(p, vec2(1, 1))
                if not sw in grid:
                    p = sw
                    continue
                

                grid[p] = "*"
                #print_grid(grid, (40, 20), (480, 0), width=1, separator="")
                break

        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [[int(d) for d in digit_re.findall(line)] for line in file]
        groups = [list(vec2(x, y) for [x, y] in chunk(l, 2)) for l in lines]
        
        grid = {} #{vec2(500, 0): "v"}
        for group in groups:
            for a, b in zip(group, group[1:]):
                for point in aaline(a, b):
                    grid[point] = "#"
                    #print(point)

        lowest_y = max(p.y for p in grid)

        fl = lowest_y + 2
        for i in range(-1000, 1000):
            grid[vec2(i, fl)] = "#"

        for i in count():
            p = vec2(500, 0)
            if p in grid:
                print_grid(grid, (40, 20), (480, 0), width=1, separator="")
                print(i)
                return True

            while True:

                south = add_t(p, vec2(0, 1))
                if not south in grid:
                    p = south
                    continue
                se = add_t(p, vec2(-1, 1))
                if not se in grid:
                    p = se
                    continue
                sw = add_t(p, vec2(1, 1))
                if not sw in grid:
                    p = sw
                    continue
                

                grid[p] = "*"
                #print_grid(grid, (40, 20), (480, 0), width=1, separator="")
                break


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)