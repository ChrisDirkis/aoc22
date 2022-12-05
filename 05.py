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

def move(stacks, f, t):
    item = stacks[f][-1]
    stacks[f] = stacks[f][:-1]
    stacks[t].append(item)
    return stacks

def move_n(stacks, f, t, c):
    for i in range(int(c)):
        stacks = move(stacks, int(f) - 1, int(t) - 1)
    return stacks

    
def move_n_2(stacks, f, t, c):
    items = stacks[f][-c:]
    stacks[f] = stacks[f][:-c]
    for item in items:
        stacks[t].append(item)
    return stacks

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        parts = file.read().split("\n\n")
        top = parts[0].split("\n")
        width = len(top[0]) // 4 + 1
        rtop = [[line[n * 4 + 1] for n in range(width)] for line in reversed(top[:-1])] 

        stacks_u = list(zip(*rtop))
        stacks = [[c for c in stack if c != ' '] for stack in stacks_u]

        for line in parts[1].split("\n"):
            c, f, t = digit_re.findall(line)
            stacks = move_n(stacks, f, t, c)

        print("".join(stack[-1] for stack in stacks))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        parts = file.read().split("\n\n")
        top = parts[0].split("\n")
        width = len(top[0]) // 4 + 1
        rtop = [[line[n * 4 + 1] for n in range(width)] for line in reversed(top[:-1])] 

        stacks_u = list(zip(*rtop))
        stacks = [[c for c in stack if c != ' '] for stack in stacks_u]

        for line in parts[1].split("\n"):
            c, f, t = digit_re.findall(line)
            stacks = move_n_2(stacks, int(f) - 1, int(t) - 1, int(c))
            
        print("".join(stack[-1] for stack in stacks))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)