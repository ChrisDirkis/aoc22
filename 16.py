from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict, deque 
import time

from grid import *

digit_re = re.compile(r"([A-Z][A-Z])")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        filelines = file.readlines()
        lines = [[pair for pair in digit_re.findall(line)] for line in filelines]
        valves = {line[0]: line[1:] for line in lines}
        r = zip([line[0] for line in lines], [int(re.findall(r"(\d+)", line)[0]) for line in filelines])
        rates = {rate[0]: rate[1] for rate in r}

        print(valves)
        print(rates)

        frontier = deque()
        frontier.append((0, "AA", set(), 0))

        maxf = 0

        useful_valves = [v for v in valves if rates[v] > 0]

        costs = dict()
        for valve in valves:
            _, shortest = djikstra(valve, None, lambda v: valves[v])
            for end in shortest:
                costs[(valve, end)] = shortest[end]   

        while frontier:
            s, n, o, sc = frontier.popleft()

            for v in useful_valves:
                if v in o: continue
                ns = s + costs[(n, v)] + 1

                if ns > 30: continue

                nv, no = v, o | {v}
                nsc = sc + rates[v] * (30 - ns)
                
                if nsc > maxf:
                    maxf = nsc
                    print(nsc)

                frontier.append((ns, nv, no, nsc))
        pass


def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        filelines = file.readlines()
        lines = [[pair for pair in digit_re.findall(line)] for line in filelines]
        valves = {line[0]: line[1:] for line in lines}
        r = zip([line[0] for line in lines], [int(re.findall(r"(\d+)", line)[0]) for line in filelines])
        rates = {rate[0]: rate[1] for rate in r}

        print(valves)
        print(rates)

        frontier = deque()
        frontier.append((0, ("AA", 0), ("AA", 0), set(), 0, []))

        maxf = 0

        useful_valves = [v for v in valves if rates[v] > 0]

        costs = dict()
        for valve in valves:
            _, shortest = djikstra(valve, None, lambda v: valves[v])
            for end in shortest:
                costs[(valve, end)] = shortest[end] + 1

        t = time.time()
        def explore(mnode, mtarget, enode, etarget, sc, rem: set):
            nonlocal maxf
            nonlocal t

            # I'm always the closest
            if etarget > mtarget:
                mnode, enode = enode, mnode
                mtarget, etarget = etarget, mtarget

            if mtarget <= 0: return

            # apply rate
            sc += rates[mnode] * mtarget

            nmaxf = max(maxf, sc)
            if nmaxf > maxf:
                maxf = nmaxf
                print(nmaxf)

            if len(rem) == 0:
                # I'm the last one
                explore(None, -1, enode, etarget, sc, set())

            # pick new target
            for node in rem:
                explore(node, mtarget - costs[(mnode, node)], enode, etarget, sc, rem - {node})
                
                if enode == "AA":
                    print(f"finished node {node}, +{time.time() - t:.1f}s")
                    t = time.time()
                
        explore("AA", 26, "AA", 26, 0, set(useful_valves))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)