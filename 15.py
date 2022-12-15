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
            return all(dist_taxi(s, p) > dist_taxi(s, b) for s, b in rows)
        
        def in_range(p):
            return p.x >= mi and p.x <= ma and p.y >= mi and p.y <= ma
        
        def lines_intersect(l1, l2):
            a, b = l1
            c, d = l2
            ax, ay = a
            bx, by = b
            cx, cy = c
            dx, dy = d

            u=(bx*(cy-ay) +by*(ax-cx))/(dx*by-dy*bx)
            t=(dx*(ay-cy) +dy*(cx-ax))/(bx*dy-by*dx)

            s1 =  vec2(cx+u*dx, cy+u*dy)
            s2 = vec2(ax+t*bx, ay+t*by)
            if s1 != s2:
                print("fuck")
            return s1
            
        for s1, b1 in rows:
            for s2, b2 in rows:
                if s1 == s2:
                    continue

                d1 = dist_taxi(s1, b1)
                d2 = dist_taxi(s2, b2)

                l11 = (vec2(s1.x + d1 + 1, s1.y), vec2(1, -1))
                l12 = (vec2(s1.x, s1.y + d1 + 1), vec2(-1, -1))
                l13 = (vec2(s1.x - d1 - 1, s1.y), vec2(-1, 1))
                l14 = (vec2(s1.x, s1.y - d1 - 1), vec2(1, 1))

                l21 = (vec2(s2.x + d2 + 1, s2.y), vec2(1, -1))
                l22 = (vec2(s2.x, s2.y + d2 + 1), vec2(-1, -1))
                l23 = (vec2(s2.x - d2 - 1, s2.y), vec2(-1, 1))
                l24 = (vec2(s2.x, s2.y - d2 - 1), vec2(1, 1))

                p1 = lines_intersect(l14, l21)
                p2 = lines_intersect(l11, l24)
                p3 = lines_intersect(l12, l21)
                p4 = lines_intersect(l11, l22)
                p5 = lines_intersect(l23, l12)
                p6 = lines_intersect(l22, l13)
                p7 = lines_intersect(l24, l13)
                p8 = lines_intersect(l23, l14)

                p9 = lines_intersect(l11, l12)
                p10 = lines_intersect(l12, l13)
                p11 = lines_intersect(l13, l14)
                p12 = lines_intersect(l14, l11)

                p13 = lines_intersect(l21, l22)
                p14 = lines_intersect(l22, l23)
                p15 = lines_intersect(l23, l24)
                p16 = lines_intersect(l24, l21)


                for p in [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]:
                    if p.x != int(p.x) or p.y != int(p.y):
                        continue
                    p = vec2(int(p.x), int(p.y))
                    if in_range(p) and test(p):
                        print(p)
                        print(freq(p))
                        return

        

if __name__ == "__main__":
    #part_1(testing_file_name)
    #part_1(data_file_name)
    #part_2(testing_file_name)
    part_2(data_file_name)