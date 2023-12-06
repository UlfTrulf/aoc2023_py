import numpy as np
import regex as re
from sympy.solvers import solve
from sympy import Symbol


def calc_num_record(race_time, distance):
    x = Symbol("x")
    s = solve(x * race_time - x ** 2 - distance)
    return np.floor(s[1] - s[0])


def reader1(txt):
    data = []
    for line in open(txt):
        (data.append(list(map(int, re.findall(r'\d+', line)))))
    return data


def part1(txt):
    data = reader1(txt)
    records = []
    race_number = 0
    while race_number < len(data[0]):
        records.append(calc_num_record(data[0][race_number], data[1][race_number]))
        race_number += 1
    return np.prod(records)


def reader2(txt):
    data = []
    for line in open(txt):
        (data.append(list(map(int, re.findall(r'\d+', line.replace(' ', ''))))))
    return data


def part2(txt):
    data = reader2(txt)
    return calc_num_record(data[0][0], data[1][0])
