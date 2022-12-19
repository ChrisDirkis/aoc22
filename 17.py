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

rocks = [
    ["####"],
    [" # ", "###", " # "],
    ["  #", "  #", "###"],
    ["#","#","#","#"],
    ["##","##"],
]

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        steps = file.read().strip()


        grid = {(i, -1): "=" for i in range(7)}
        def check_grid(x, y): return (x, y) in grid and grid[(x, y)] != " "

        def pg():
            
            m = max(y for x, y in grid) + 1
            for i in range(7):
                for j in range(m):
                    if (i, j) not in grid:
                        grid[(i, j)] = " "

            print_grid(grid, (7, m), separator="", flip_y=True)


        def can_move(rock, x, y, dir):
            if dir.x == 1 and x + len(rock[0]) > 6:
                return False
            
            if dir.x == -1 and x == 0:
                return False
            
            for j, row in enumerate(reversed(rock)):
                for i, c in enumerate(row):
                    coord = (x + i + dir[0], y + j + dir[1])
                    if c != " " and check_grid(*coord):
                        return False
            return True


        ptr = 0
        for i in range(2022):
            #pg()
            #print("=======")
            rock = rocks[i % len(rocks)]
            y = max(y for x, y in grid) + 4
            x = 2
            while True:
                jet = steps[ptr % len(steps)]
                ptr += 1
                jet_dir = vec2(-1, 0) if jet == "<" else vec2(1, 0)
                if can_move(rock, x, y, jet_dir):
                    x += jet_dir.x
                    #print(f"moved {jet_dir}")

                if can_move(rock, x, y, vec2(0, -1)):
                    y -= 1
                    #print("dropped")
                else:
                    # apply rock
                    for j, row in enumerate(reversed(rock)):
                        for i, c in enumerate(row):
                            coord = (x + i, y + j)
                            if c == "#":
                                grid[coord] = "#"
                    break


        print(max(y for x, y in grid))


        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        steps = file.read().strip()

        highest = [-1 for _ in range(7)]

        grid = {(i, -1): "=" for i in range(7)}
        def check_grid(x, y): return (x, y) in grid and grid[(x, y)] != " "
        def set_grid(x, y):
            grid[(x, y)] = "#"
            highest[x] = max(highest[x], y)
        

        def pg():
            
            m = max(y for x, y in grid) + 1
            for i in range(7):
                for j in range(m):
                    if (i, j) not in grid:
                        grid[(i, j)] = " "

            print_grid(grid, (7, m), separator="", flip_y=True)


        def can_move(rock, x, y, dir):
            if dir.x == 1 and x + len(rock[0]) > 6:
                return False
            
            if dir.x == -1 and x == 0:
                return False
            
            for j, row in enumerate(reversed(rock)):
                for i, c in enumerate(row):
                    coord = (x + i + dir[0], y + j + dir[1])
                    if c != " " and check_grid(*coord):
                        return False
            return True

        def h(y):
            ha = 0
            for j in range(y - 8 + 1, y + 1):
                for i in range(7):
                    ha += 31 if (i, j) in grid else 37
                    ha *= 41
                    ha %= 2**32
            return ha

        history = {}
        ptr = 0
        r = 0
        for i in range(1000000000000):

            if i > 100:
                state = (ptr % len(steps), r % len(rocks), h(max(highest)))
                if state in history:
                    # print(f"owo {i}")
                    # print_grid(grid, (8, 7), offset=(0, max(highest) - 8), separator="", flip_y=True)
                    # print("===")
                    # print_grid(grid, (8, 7), offset=(0, history[state][0] - 8), separator="", flip_y=True)
                    break
                else:
                    history[state] = (max(highest), i)

            #pg()
            #print("=======")
            rock = rocks[r % len(rocks)]
            r += 1
            r %= len(rocks)

            y = max(highest) + 4
            x = 2
            while True:
                jet = steps[ptr % len(steps)]
                ptr += 1
                ptr %= len(steps)
                jet_dir = vec2(-1, 0) if jet == "<" else vec2(1, 0)
                if can_move(rock, x, y, jet_dir):
                    x += jet_dir.x
                    #print(f"moved {jet_dir}")

                if can_move(rock, x, y, vec2(0, -1)):
                    y -= 1
                    #print("dropped")
                else:
                    # apply rock
                    for j, row in enumerate(reversed(rock)):
                        for i, c in enumerate(row):
                            if c == "#":
                                set_grid(x + i, y + j)
                    break
        
        height, index = history[state]
        dh = max(highest) - height
        di = i - index


        mh = max(highest)
        print(di, dh)
        free_loops = (1000000000000 - i) // di
        print(f"skipped {free_loops} loops ({free_loops * di} steps)")

        for j in range(-1, 50):
            for x in range(7):
                if (x, mh - j) in grid:
                    grid[(x, free_loops * dh + mh - j)] =  grid[(x, mh - j)] 
            
        
        for x in range(6):
            highest[x] += free_loops * dh
        i += free_loops * di


        blocks_remaining = 1000000000000 - i


        for i in range(blocks_remaining):
            
            rock = rocks[r % len(rocks)]
            r += 1
            r %= len(rocks)
            
            y = max(highest) + 4
            x = 2
            while True:
                jet = steps[ptr % len(steps)]
                ptr += 1
                ptr %= len(steps)
                jet_dir = vec2(-1, 0) if jet == "<" else vec2(1, 0)
                if can_move(rock, x, y, jet_dir):
                    x += jet_dir.x
                    #print(f"moved {jet_dir}")

                if can_move(rock, x, y, vec2(0, -1)):
                    y -= 1
                    #print("dropped")
                else:
                    # apply rock
                    for j, row in enumerate(reversed(rock)):
                        for i, c in enumerate(row):
                            if c == "#":
                                set_grid(x + i, y + j)
                    break



        print(max(highest) + 1)

        pass

if __name__ == "__main__":
    #part_1(testing_file_name)
    #part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)