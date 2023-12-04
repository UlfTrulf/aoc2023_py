from collections import Counter
import regex


def reader(line):
    li = line.split(':')
    cn = int(li[0].split(' ')[-1])
    c = li[1].split('|')
    h = regex.findall(r'\d+', c[0])
    n = regex.findall(r'\d+', c[1])
    return cn, h, n


def count_hits(a, b):
    ca = Counter(a)
    cb = Counter(b)
    return sum(v <= ca[k] for k, v in cb.items())


def part1(txt):
    f = open(txt)
    s = 0
    for line in f:
        cn, h, n = reader(line)
        sh = count_hits(h, n)
        if sh > 0:
            s += 2 ** (sh - 1)
    return s


def part2(txt):
    f = open(txt)
    hits = []
    for line in f:
        cn, h, n = reader(line)
        hits.append([1, count_hits(h, n)])
    i = 0
    s = 0
    while len(hits) > i:
        j = 1
        while j <= hits[i][1] and j + i < len(hits):
            hits[i+j][0] += hits[i][0]
            j += 1
        s += hits[i][0]
        i += 1
    return s
