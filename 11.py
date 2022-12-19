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

def mul(b):
    return lambda a: a * b
def add(b):
    return lambda a: a + b
def mul_s():
    return lambda s: s * s

def apply(worry, oper):
    if oper == "sq":
        return worry * worry
    elif oper[0] == "mul":
        return worry * oper[1]
    elif oper[0] == "add":
        return worry + oper[1]

def mon(mt):
    mt = [l.strip() for l in mt.split("\n")]
    items = [int(d) for d in digit_re.findall(mt[1])]
    div_test = [int(d) for d in digit_re.findall(mt[3])][0]
    true_throw = [int(d) for d in digit_re.findall(mt[4])][0]
    false_throw = [int(d) for d in digit_re.findall(mt[5])][0]

    oper_t = mt[2]
    if oper_t[-3:] == "old":
        oper = "sq"
    elif "*" in oper_t:
        oper = ("mul", int(oper_t.split("*")[1]))
    elif "+" in oper_t:
        oper = ("add", int(oper_t.split("+")[1]))

    return (items, oper, div_test, true_throw, false_throw)

def part_1(filename):
    print(f"Part 1: {filename}")
    with open(filename) as file:
        mts = file.read().split("\n\n")
        monkeys = [mon(mt) for mt in mts]

        inspections = [0 for m in monkeys]

        for r in range(20):
            for i in range(len(monkeys)):
                monkey = monkeys[i]
                items, oper, div_test, true_throw, false_throw = monkey
                for item in items:
                    inspections[i] += 1
                    item = apply(item, oper) // 3
                    if item % div_test == 0:
                        monkeys[true_throw][0].append(item)
                    else:
                        monkeys[false_throw][0].append(item)
                
                monkeys[i] = ([], oper, div_test, true_throw, false_throw)


        print(prod(list(sorted(inspections))[-2:]))
        pass

def part_2(filename):
    print(f"Part 2: {filename}")
    with open(filename) as file:
        mts = file.read().split("\n\n")
        monkeys = [mon(mt) for mt in mts]

        inspections = [0 for m in monkeys]
        p = prod(m[2] for m in monkeys)
        for r in range(10000):
            for i in range(len(monkeys)):
                monkey = monkeys[i]
                items, oper, div_test, true_throw, false_throw = monkey
                for item in items:
                    inspections[i] += 1

                    item = apply(item, oper)


                    if item % div_test == 0:
                        next = monkeys[true_throw]
                    else:
                        next = monkeys[false_throw]

                    item %= p

                    next[0].append(item)


                
                monkeys[i] = ([], oper, div_test, true_throw, false_throw)



        print(prod(list(sorted(inspections))[-2:]))
        pass

if __name__ == "__main__":
    part_1(testing_file_name)
    part_1(data_file_name)
    part_2(testing_file_name)
    part_2(data_file_name)