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

adj8s = [
    vec2(-1, -1),
    vec2(-1, 0),
    vec2(-1, 1),
    vec2(0, -1),
    vec2(0, 1),
    vec2(1, -1),
    vec2(1, 0),
    vec2(1, 1),
]
def adj8(v):
    for d in adj8s:
        yield add_t(v, d)

def pg(grid):
    
    min_x = min(grid, key=lambda v: v.x).x
    max_x = max(grid, key=lambda v: v.x).x
    min_y = min(grid, key=lambda v: v.y).y
    max_y = max(grid, key=lambda v: v.y).y
    s = 0
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            ig = vec2(i, j) in grid
            print(grid[vec2(i, j)] if ig else ".", end="")
            if not ig: s += 1
        print()
    print(s)

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        g = [list(line.strip()) for line in file]
        dims = vec2(len(g[0]), len(g))

        grid = {}
        for j in range(dims.y):
            for i in range(dims.x):
                if g[j][i] == "#":
                    grid[vec2(i, j)] = g[j][i]
        
        dirs = [
            (vec2(0, -1), [vec2(0, -1), vec2(-1, -1), vec2(1, -1)]),
            (vec2(0, 1), [vec2(0, 1), vec2(-1, 1), vec2(1, 1)]),
            (vec2(-1, 0), [vec2(-1, 0), vec2(-1, 1), vec2(-1, -1)]),
            (vec2(1, 0), [vec2(1, 0), vec2(1, 1), vec2(1, -1)]),
        ]

        for i in range(10):
            potential = {}
            for fro in grid:
                
                if not any(a in grid for a in adj8(fro)): continue

                for d, ds in dirs:
                    if not any(add_t(fro, x) in grid for x in ds):
                        to = add_t(fro, d) 
                        if to in potential:
                            potential[to].append(fro)
                        else:
                            potential[to] = [fro]
                        break
            

            for to in potential:
                froms = potential[to]
                if len(froms) == 1:
                    fro = froms[0]
                    del grid[fro]
                    grid[to] = "#"
            
            dirs = dirs[1:] + [dirs[0]]
            #pg(grid)
            #print()

        

        min_x = min(grid, key=lambda v: v.x).x
        max_x = max(grid, key=lambda v: v.x).x
        min_y = min(grid, key=lambda v: v.y).y
        max_y = max(grid, key=lambda v: v.y).y

        s = 0
        for j in range(min_y, max_y + 1):
            for i in range(min_x, max_x + 1):
                s += 1 if vec2(i, j) not in grid else 0  
        print(s)

        pass



def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file: 
        g = [list(line.strip()) for line in file]
        dims = vec2(len(g[0]), len(g))

        grid = {}
        for j in range(dims.y):
            for i in range(dims.x):
                if g[j][i] == "#":
                    grid[vec2(i, j)] = g[j][i]
        
        dirs = [
            (vec2(0, -1), [vec2(0, -1), vec2(-1, -1), vec2(1, -1)]),
            (vec2(0, 1), [vec2(0, 1), vec2(-1, 1), vec2(1, 1)]),
            (vec2(-1, 0), [vec2(-1, 0), vec2(-1, 1), vec2(-1, -1)]),
            (vec2(1, 0), [vec2(1, 0), vec2(1, 1), vec2(1, -1)]),
        ]

        for i in count():
            potential = {}
            for fro in grid:
                
                if not any(a in grid for a in adj8(fro)): continue

                for d, ds in dirs:
                    if not any(add_t(fro, x) in grid for x in ds):
                        to = add_t(fro, d) 
                        if to in potential:
                            potential[to] = False
                        else:
                            potential[to] = fro
                        break

            if len(potential) == 0:
                print(i)
                return
            

            for to in potential:
                fro = potential[to]
                if fro:
                    del grid[fro]
                    grid[to] = "#"
            
            dirs = dirs[1:] + [dirs[0]]
            #pg(grid)
            #print()

        

        min_x = min(grid, key=lambda v: v.x).x
        max_x = max(grid, key=lambda v: v.x).x
        min_y = min(grid, key=lambda v: v.y).y
        max_y = max(grid, key=lambda v: v.y).y

        s = 0
        for j in range(min_y, max_y + 1):
            for i in range(min_x, max_x + 1):
                s += 1 if vec2(i, j) not in grid else 0  
        print(s)

        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)