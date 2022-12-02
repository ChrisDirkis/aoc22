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

opp = {
    "A": 0,
    "B": 1,
    "C": 2,
}

me = {
    "X": 0,
    "Y": 1,
    "Z": 2,
}

rme = {
    0: "X",
    1: "Y",
    2: "Z",
}

def score(a, x):
    oh, mh = opp[a], me[x]
    s = mh + 1
    if (oh + 1) % 3 == mh:
        s += 6
    elif oh == mh:
        s += 3
    return s

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [tuple(line.strip().split(" ")) for line in file]
        scores = [score(a, b) for a, b in lines]
        print(sum(scores))
        pass

def get_play(line):
    oh = opp[line[0]]
    outcome = line[1]
    if outcome == "X":
        return (line[0], rme[(oh - 1 + 3) % 3])
    if outcome == "Y":
        return (line[0], rme[oh])
    if outcome == "Z":
        return (line[0], rme[(oh + 1) % 3])

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [tuple(line.strip().split(" ")) for line in file]
        plays = [get_play(line) for line in lines]
        scores = [score(a, b) for a, b in plays]
        print(sum(scores))

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)