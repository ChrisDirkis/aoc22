from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict, deque
import sys

from grid import *

digit_re = re.compile(r"(\d+)")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"


ro = ["ore", "clay", "obsidian", "geode"]
def orei(name):
    if name == "ore": return 0
    elif name == "clay": return 1
    elif name == "obsidian": return 2
    else: return 3

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [[s.strip() for s in l.split(":")[1].split(".") if len(s.strip()) > 0] for l in file.read().split("\n")]
        cost_re = re.compile(r"(\d+) ([A-z]+)")
        dirty_bps = [[cost_re.findall(step) for step in bp] for bp in lines]
        bps = [[[(int(sc[0]), sc[1]) for sc in step] for step in dbp] for dbp in dirty_bps]
        bps2 = [[[0, 0, 0, 0] for i in range(4)] for bp in bps]
        for bp, bp2 in zip(bps, bps2):
            for recipe, r2 in zip(bp, bp2):
                for cost, mat in recipe:
                    r2[orei(mat)] += cost
    

        qual = 0
        for id, blueprint in enumerate(bps2):
            

            maxg = 0
            @cache
            def dfs(a, b, c, d, time, e, f, g, h):
                nonlocal maxg
                robots = [a, b, c, d]
                stuff = [e, f, g, h]
                maxg = max(maxg, stuff[3] + (time - 1) * robots[3])

                for i, recipe in enumerate(blueprint):
                    if any(robots[v] == 0 and recipe[v] != 0 for v in range(4)): continue
                    time_till_recipe = max(ceil((recipe[v] - stuff[v]) / robots[v]) if recipe[v] > 0 else 0 for v in range(4)) + 1

                    if time_till_recipe > time: continue

                    nt, nr, ns = time, list(robots), list(stuff)

                    nt -= time_till_recipe
                    for v in range(4):
                        ns[v] += nr[v] * time_till_recipe
                        ns[v] -= recipe[v]
                    nr[i] += 1

                    dfs(nr[0], nr[1], nr[2], nr[3], nt, ns[0], ns[1], ns[2], ns[3])
                    if time == 15:
                        print(f"done with recipe {i}")

            dfs(1, 0, 0, 0, 15, 0, 0, 0, 0)
            qual += maxg * (id + 1)
            
        print(qual)


                

            



        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)