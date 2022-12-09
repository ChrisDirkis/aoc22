from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from grid import *

digit_re = re.compile(r"(\d)")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [[int(c) for c in line.strip()] for line in file]

        visible = [[False for d in line] for line in lines]

        #left/right
        for j, line in enumerate(lines):
            outside = -1
            for i, d in enumerate(line):
                if d > outside:
                    visible[j][i] = True
                    outside = d
            outside = -1
            for i, d in reversed(list(enumerate(line))):
                if d > outside:
                    visible[j][i] = True
                    outside = d

        # top/bottom
        for i in range(len(lines[0])):
            outside = -1
            for j in range(len(lines)):
                d = lines[j][i]
                if d > outside:
                    visible[j][i] = True
                    outside = d
            outside = -1
            for j in reversed(list(range(len(lines)))):
                d = lines[j][i]
                if d > outside:
                    visible[j][i] = True
                    outside = d


        
        print(sum(sum(line) for line in visible))
        pass

def score(grid, dims, i, j):
    p = grid[(i, j)]
    if i == 0 or j == 0 or i == dims[0] - 1 or j == dims[1] - 1:
        return 0
    #down
    d = 0
    for d, y in enumerate(range(j + 1, dims[1])):
        if grid[(i, y)] >= p:
            break
    d += 1
    
    #up
    u = 0
    for u, y in enumerate(range(j - 1, -1, -1)):
        if grid[(i, y)] >= p:
            break
    u += 1
    
    #down
    l = 0
    for l, x in enumerate(range(i + 1, dims[1])):
        if grid[(x, j)] >= p:
            break
    l += 1
    
    #down
    r = 0
    for r, x in enumerate(range(i - 1, -1, -1)):
        if grid[(x, j)] >= p:
            break
    r += 1

    #print(p, (i, j), d, u, l, r)

    return d * u * l * r

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [[int(c) for c in line.strip()] for line in file]

        for line in lines:
            print(line)

        dims = (len(lines[0]), len(lines))

        grid = {}
        for j in range(len(lines)):
            for i in range(len(lines[j])):
                d = lines[j][i]
                grid[(i, j)] = d
        
        print(max(score(grid, dims, i, j) for i, j in grid))



if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)