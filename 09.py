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

dirs = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

def sign(a):
    if a == 0:
        return 0
    return -1 if a < 0 else 1

def move(h, t, dir):
    nh = add_t(h, dir)
    return nh, constrain(nh, t)

def constrain(a, b):
    if a == b:
        return b
    
    if b.y == a.y:
        if a.x - b.x > 1:
            b = vec2(a.x - 1, b.y)
        if a.x - b.x < -1:
            b = vec2(a.x + 1, b.y)
    elif b.x == a.x:
        if a.y - b.y > 1:
            b = vec2(b.x, a.y - 1)
        if a.y - b.y < -1:
            b = vec2(b.x, a.y + 1)
    elif abs(b.x - a.x) > 1 or abs(b.y - a.y) > 1:
        b = vec2(b.x + sign(a.x - b.x), b.y + sign(a.y - b.y))
    return b

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [line.strip().split(" ") for line in file]
        h = vec2(0, 0)
        t = vec2(0, 0)
        s = {t}
        for line in lines:
            for i in range(int(line[1])):
                dir = dirs[line[0]]
                h, t = move(h, t, dir)
                s.add(t)
        print(len(s))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [line.strip().split(" ") for line in file]
        rope = [vec2(0, 0) for i in range(10)]
        s = [rope[9]]
        for line in lines:
            for i in range(int(line[1])):
                dir = dirs[line[0]]
                rope[0] = add_t(rope[0], dir)
                for i in range(9):
                    rope[i + 1] = constrain(rope[i], rope[i + 1])
                s.append(rope[9])
        print(len(set(s)))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)