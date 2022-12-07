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


def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        path = []
        fs = {}
        dirs = []
        lines = file.readlines()
        i = 1
        while i < len(lines):
            line = lines[i].strip()
            sline = line.split(" ")
            #print(line)
            if sline[1] == "cd":
                if sline[2] == "..":
                    path = path[:-1]
                else:
                    path.append(sline[2])
                i += 1
            elif sline[1] == "ls":
                j = 1
                while  i+j < len(lines) and lines[i+j][0] != "$" :
                    sline2 = lines[i+j].strip().split(" ")
                    p = "/".join(path) + "/" + sline2[1] if len(path) == 0 else "/" + "/".join(path) + "/" + sline2[1]
                    if sline2[0] != "dir":
                        fs[p] = int(sline2[0])
                    else:
                        dirs.append(p)
                    j += 1
                i += j
        #print(fs)

        dir_sizes = [sum(fs[file] for file in fs if file.startswith(dir)) for dir in dirs]
        print(sum(s for s in dir_sizes if s < 100000))
            




                

        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        path = []
        fs = {}
        dirs = []
        lines = file.readlines()
        i = 1
        while i < len(lines):
            line = lines[i].strip()
            sline = line.split(" ")
            #print(line)
            if sline[1] == "cd":
                if sline[2] == "..":
                    path = path[:-1]
                else:
                    path.append(sline[2])
                i += 1
            elif sline[1] == "ls":
                j = 1
                while  i+j < len(lines) and lines[i+j][0] != "$" :
                    sline2 = lines[i+j].strip().split(" ")
                    p = "/".join(path) + "/" + sline2[1] if len(path) == 0 else "/" + "/".join(path) + "/" + sline2[1]
                    if sline2[0] != "dir":
                        fs[p] = int(sline2[0])
                    else:
                        dirs.append(p)
                    j += 1
                i += j
        #print(fs)

        dir_sizes = [sum(fs[file] for file in fs if file.startswith(dir)) for dir in dirs]

        used = sum(fs[f] for f in fs)
        total = 70000000
        unused = total - used
        needed = 30000000 - unused
        dir_s = zip(dir_sizes, dirs)
        print(next((s, d) for s, d in sorted(dir_s) if s > needed))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)