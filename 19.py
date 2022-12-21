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
            
            max_recipe_costs = [max(recipe[v] for recipe in blueprint) for v in range(3)]

            @cache
            def dfs(ore, cla, obs, time, ore_b, cla_b, obs_b):
                robots = [ore, cla, obs]
                stuff = [ore_b, cla_b, obs_b]

                geodes = 0
                for i, recipe in enumerate(blueprint):
                    #funroll
                    if robots[0] == 0 and recipe[0] != 0: continue
                    if robots[1] == 0 and recipe[1] != 0: continue
                    if robots[2] == 0 and recipe[2] != 0: continue

                    # berk

                    if i != 3: 
                        if time <= 5: continue
                        if robots[i] == max_recipe_costs[i]: continue

                    #funroll
                    min_times_1 = ceil((recipe[0] - stuff[0]) / robots[0]) if recipe[0] > 0 else 0
                    min_times_2 = ceil((recipe[1] - stuff[1]) / robots[1]) if recipe[1] > 0 else 0
                    min_times_3 = ceil((recipe[2] - stuff[2]) / robots[2]) if recipe[2] > 0 else 0
                    time_till_recipe = max(0, min_times_1, min_times_2, min_times_3) + 1

                    if time_till_recipe > time: continue

                    nt, nr, ns = time, list(robots), list(stuff)

                    nt -= time_till_recipe

                    #funroll
                    ns[0] += nr[0] * time_till_recipe
                    ns[0] -= recipe[0]
                    ns[1] += nr[1] * time_till_recipe
                    ns[1] -= recipe[1]
                    ns[2] += nr[2] * time_till_recipe
                    ns[2] -= recipe[2]

                    if nr[0] == max_recipe_costs[0]:
                        ns[0] = max_recipe_costs[0]
                    if nr[1] == max_recipe_costs[1]:
                        ns[1] = max_recipe_costs[1]
                    if nr[2] == max_recipe_costs[2]:
                        ns[2] = max_recipe_costs[2]

                    if i == 3:
                        geodes_this_turn = nt - 1
                    else:
                        nr[i] += 1
                        geodes_this_turn = 0

                    geodes = max(geodes, geodes_this_turn + dfs(nr[0], nr[1], nr[2], nt, ns[0], ns[1], ns[2]))
                    # if time == 25:
                    #     print(f"done with recipe {i}")
                return geodes

            geodes = dfs(1, 0, 0, 25, 0, 0, 0)
            print(f"recipe {id + 1}: {geodes}")
            qual += geodes * (id + 1)
            
        print(qual)


        pass

def part_2(filename):
    print(f"Part 2: {filename}")
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
    
        qual = 1
        for id, blueprint in enumerate(bps2[:3]):

            max_recipe_costs = [max(recipe[v] for recipe in blueprint) for v in range(3)]

            @cache
            def dfs(ore, cla, obs, time, ore_b, cla_b, obs_b):
                
                # berk
                if time < 20 and ore_b < max_recipe_costs[0]: return 0 

                robots = [ore, cla, obs]
                stuff = [ore_b, cla_b, obs_b]

                geodes = 0
                for i, recipe in enumerate(blueprint):
                    #funroll
                    if robots[0] == 0 and recipe[0] != 0: continue
                    if robots[1] == 0 and recipe[1] != 0: continue
                    if robots[2] == 0 and recipe[2] != 0: continue

                    # berk
                    if time < 20 and i == 0: continue 
                    if i != 3: 
                        if time <= 4: continue
                        if robots[i] == max_recipe_costs[i]: continue

                    #funroll
                    min_times_1 = ceil((recipe[0] - stuff[0]) / robots[0]) if recipe[0] > 0 else 0
                    min_times_2 = ceil((recipe[1] - stuff[1]) / robots[1]) if recipe[1] > 0 else 0
                    min_times_3 = ceil((recipe[2] - stuff[2]) / robots[2]) if recipe[2] > 0 else 0
                    time_till_recipe = max(0, min_times_1, min_times_2, min_times_3) + 1

                    if time_till_recipe > time: continue

                    nt, nr, ns = time, list(robots), list(stuff)

                    nt -= time_till_recipe

                    #funroll
                    ns[0] += nr[0] * time_till_recipe
                    ns[0] -= recipe[0]
                    ns[1] += nr[1] * time_till_recipe
                    ns[1] -= recipe[1]
                    ns[2] += nr[2] * time_till_recipe
                    ns[2] -= recipe[2]

                    if nr[0] == max_recipe_costs[0]:
                        ns[0] = max_recipe_costs[0]
                    if nr[1] == max_recipe_costs[1]:
                        ns[1] = max_recipe_costs[1]
                    if nr[2] == max_recipe_costs[2]:
                        ns[2] = max_recipe_costs[2]

                    if i == 3:
                        geodes_this_turn = nt - 1
                    else:
                        nr[i] += 1
                        geodes_this_turn = 0

                    geodes = max(geodes, geodes_this_turn + dfs(nr[0], nr[1], nr[2], nt, ns[0], ns[1], ns[2]))
                    if time == 32:
                        print(f"done with recipe {i}")
                return geodes

            geodes = dfs(1, 0, 0, 32, 0, 0, 0)
            print(f"recipe {id + 1}: {geodes}")
            qual *= geodes
            
        print(qual)

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)