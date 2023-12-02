import numpy as np


col_dict = {
    'red': 0,
    'green': 1,
    'blue': 2
}


def convert_subset(sub):
    k = sub.split(' ')
    i = 1
    c = [0, 0, 0]
    while i < len(k):
        c[col_dict.get(k[i + 1].replace(',', '').replace('\n', ''))] = int(k[i])
        i += 2
    return c


def reader(line):
    l = line.split(':')
    n = int(l[0].split(' ')[1])
    ss = l[1].split(';')
    return l, n, ss


def part1():
    f = open('input/day02.txt')
    s = 0
    for line in f:
        l, n, ss = reader(line)
        limit = True
        for subset in ss:
            c = convert_subset(subset)
            if c[0] > 12 or c[1] > 13 or c[2] > 14:
                limit = False
        if limit:
            s += n
    print('Day2 Part1: ' + str(s))


def part2():
    f = open('input/day02.txt')
    s = 0
    for line in f:
        l, n, ss = reader(line)
        m = [0, 0, 0]
        for subset in ss:
            c = convert_subset(subset)
            i = 0
            while i < 3:
                if c[i] > m[i]:
                    m[i] = c[i]
                i += 1
        s += np.prod(m)
    print('Day2 Part2: ' + str(s))