from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict 

from grid import *

digit_re = re.compile(r"([-\d]+)")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        ty = 2000000

        lines = [[int(d) for d in digit_re.findall(line)] for line in file]
        rows = [(vec2(l[0], l[1]), vec2(l[2], l[3])) for l in lines]

        beacons = {b for s, b in rows}
        sensors = {s for s, b in rows}
        grid = {}
        for s, b in rows:
            dist = dist_taxi(s, b)
            yoff = ty - s.y
            width = max(0, dist - abs(yoff))
            if width == 0: continue
            print(s, b, dist, width)
            for x in range(s.x - width, s.x + width + 1):
                p = vec2(x, ty)
                if p not in beacons and p not in sensors:
                    grid[x] = "#"
        
        

        print(len(grid))
        
                
        pass

def part_2(filename):
    print(f"Part 2: {filename}")    
    with open(filename) as file:
        mi = 0
        ma = 4000000
        mul = 4000000

        def freq(p): return p.x * mul + p.y

        lines = [[int(d) for d in digit_re.findall(line)] for line in file]
        rows = [(vec2(l[0], l[1]), vec2(l[2], l[3])) for l in lines]

        beacons = {b for s, b in rows}
        sensors = {s for s, b in rows}

        def test(p):
            return all(dist_taxi(s, p) <= dist_taxi(s, b) for s, b in rows)
        
        def in_range(p):
            return p.x >= mi and p.x <= ma and p.y >= mi and p.y <= ma

        candidates = set()
        for s, b in rows:
            dist = dist_taxi(s, b)
            p = vec2(s.x, s.y + dist + 1) 
            print(dist, s, b)
        
            for i in range(dist + 1):
                if in_range(p):
                    if test(p):
                        print(p)
                p = add_t(p, (1, -1))

            for i in range(dist + 1):
                if in_range(p):
                    if test(p):
                        print(p)
                p = add_t(p, (-1, -1))

            for i in range(dist + 1):
                if in_range(p):
                    if test(p):
                        print(p)
                p = add_t(p, (-1, 1))

            for i in range(dist + 1):
                if in_range(p):
                    if test(p):
                        print(p)
                p = add_t(p, (1, 1))


        real = []
        for p in candidates:
            flag = True
            for s, b in rows:
                if dist_taxi(s, p) <= dist_taxi(s, b):
                    flag = False
                    break

            if flag:
                print(p)
                print(freq(p))
                real.append(p)
        

if __name__ == "__main__":
    #part_1(testing_file_name)
    #part_1(data_file_name)
    #part_2(testing_file_name)
    part_2(data_file_name)