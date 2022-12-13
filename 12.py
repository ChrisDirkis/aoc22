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
        lines = [[c for c in line.strip()] for line in file]
        graph = {}
        for j, line in enumerate(lines):
            for i, c in enumerate(line):
                if c == "S":
                    start = (i, j)
                    lines[j][i] = "a"
                if c == "E":
                    end = (i, j)
                    lines[j][i] = "z"
                graph[(i, j)] = lines[j][i] 


        dims = (len(lines[0]), len(lines))
        print(start, end, dims)
        previous_nodes, shortest_paths = djikstra(start, graph, lambda n: [adj for adj in adj4(n) if adj in graph and ord(graph[adj]) - ord(graph[n]) < 2])
        
        print(shortest_paths[end])


        # n = end
        # while n != start:
        #     graph[n] = " "
        #     n = previous_nodes[n]
        
        # print_grid(graph, dims)

        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [[c for c in line.strip()] for line in file]
        graph = {}
        for j, line in enumerate(lines):
            for i, c in enumerate(line):
                if c == "S":
                    start = (i, j)
                    lines[j][i] = "a"
                if c == "E":
                    end = (i, j)
                    lines[j][i] = "z"
                graph[(i, j)] = lines[j][i] 


        lowest = [vec2(node[0], node[1]) for node in graph if graph[node] == "a"]
        dims = (len(lines[0]), len(lines))

        def adjnodes(n):
            return (adj for adj in adj4(n) if adj in graph and ord(graph[adj]) - ord(graph[n]) > -2)

        previous_nodes, shortest_paths = djikstra(end, graph, lambda n: adjnodes(n))

        print(min(shortest_paths[l] for l in lowest if l in shortest_paths))


if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)