from itertools import *
from functools import *
from math import * 
import re
from collections import defaultdict, deque

from grid import *

digit_re = re.compile(r"(\d+)")

aod_day = __file__.split("/")[-1][-5:-3]
data_file_name = "inputs/" + aod_day
testing_file_name = data_file_name + "t"

def get_value(name, expr: str):
    if expr.isnumeric():
        return {"name": name, "value": int(expr), "type": "constant"}
    spl = expr.split(" ")
    return {"name": name, "oper": spl[1], "operands": [spl[0], spl[2]], "type": "expr"}

def get_value_2(name, expr: str):
    if expr.isnumeric():
        return {"name": name, "value": int(expr), "type": "constant"}

    spl = expr.split(" ")

    if name == "root":
        print(expr)
        return {"name": name, "oper": "=", "operands": [spl[0], spl[2]], "type": "expr"}
    return {"name": name, "oper": spl[1], "operands": [spl[0], spl[2]], "type": "expr"}

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        lines = [[p.strip() for p in line.split(":")] for line in file.readlines()]
        values = [get_value(name, expr) for [name, expr] in lines]

        unevaluated = deque([item for item in values if item["type"] != "constant"])
        evaled = {item["name"]: item["value"] for item in values if item["type"] == "constant"}

        while unevaluated:
            item = unevaluated.popleft()
            if all(operand in evaled for operand in item["operands"]):
                oper = item["oper"]
                if oper == "+":
                    evaled[item["name"]] = evaled[item["operands"][0]] + evaled[item["operands"][1]]
                if oper == "-":
                    evaled[item["name"]] = evaled[item["operands"][0]] - evaled[item["operands"][1]]
                if oper == "*":
                    evaled[item["name"]] = evaled[item["operands"][0]] * evaled[item["operands"][1]]
                if oper == "/":
                    evaled[item["name"]] = evaled[item["operands"][0]] // evaled[item["operands"][1]]
            else:
                unevaluated.append(item)
        print(evaled["root"])
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        lines = [[p.strip() for p in line.split(":")] for line in file.readlines()]
        values = [get_value_2(name, expr) for [name, expr] in lines]

        unevaluated = deque([item for item in values if item["type"] != "constant"])
        evaled = {item["name"]: item["value"] for item in values if item["type"] == "constant"}

        del evaled["humn"]

        l = len(unevaluated)
        c = 0

        while unevaluated:
            l2 = len(unevaluated)
            if l2 == l:
                c += 1
                if c == l2 + 10:
                    break
            else:
                l = l2
                c = 0

            item = unevaluated.popleft()
            [oa, ob] = item["operands"]
            if oa in evaled and ob in evaled:
                oper = item["oper"]
                if oper == "+":
                    evaled[item["name"]] = evaled[oa] + evaled[ob]
                if oper == "-":
                    evaled[item["name"]] = evaled[oa] - evaled[ob]
                if oper == "*":
                    evaled[item["name"]] = evaled[oa] * evaled[ob]
                if oper == "/":
                    evaled[item["name"]] = evaled[oa] // evaled[ob]
                if oper == "=" and len(unevaluated) == 0:
                    return evaled[oa] == evaled[ob]
            else:
                unevaluated.append(item)

        while unevaluated:
            item = unevaluated.popleft()
            [oa, ob] = item["operands"]
            name = item["name"]
            oper = item["oper"]
            if oa in evaled and not ob in evaled:
                if name in evaled:
                    if oper == "+":
                        evaled[ob] = evaled[name] - evaled[oa]
                        continue
                    if oper == "-":
                        evaled[ob] = evaled[oa] - evaled[name]
                        continue
                    if oper == "*":
                        evaled[ob] = evaled[name] // evaled[oa]
                        continue
                    if oper == "/":
                        evaled[ob] = evaled[oa] // evaled[name]
                        continue
                elif oper == "=":
                    evaled[ob] = evaled[oa]
                    continue
            elif ob in evaled and not oa in evaled:
                if name in evaled:
                    if oper == "+":
                        evaled[oa] = evaled[name] - evaled[ob]
                        continue
                    if oper == "-":
                        evaled[oa] = evaled[ob] + evaled[name]
                        continue
                    if oper == "*":
                        evaled[oa] = evaled[name] // evaled[ob]
                        continue
                    if oper == "/":
                        evaled[oa] = evaled[name] * evaled[ob] 
                        continue
                elif oper == "=":
                    evaled[oa] = evaled[ob]
                    continue
            unevaluated.append(item)

        print(evaled["humn"])
            




if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)