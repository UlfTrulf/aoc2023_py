import regex as re
import numpy as np


def reader(txt):
    with open(txt) as file:
       content = file.read().split('\n\n')
    m = []
    for c in content:
        p = []
        for k in c.split('\n'):
            x = list(map(int, re.findall(r'\d+', k)))
            if len(x):
                p.append(x)
        m.append(p)
    return(m)


def get_location(seedlist, almanac):
    l = []
    for s in seedlist:
        i = 1
        while i < len(almanac):
            for t in almanac[i]:
                if s in range(t[1], t[1] + t[2]):
                    s += t[0] - t[1]
                    break
            i += 1
        l.append(s)
    return np.min(l)


def part1(txt):
    m = reader(txt)
    return get_location(m[0][0], m)


def find_range_overlap(a, b):
    ma = max(a[0], b[0])
    mi = min((a[0] + a[1]), (b[0] + b[1]))
    ov = list(range(ma, mi))
    if len(ov):
        return ov[0], len(ov)
    else:
        return 0, 0


def find_non_overlapping(a, b):
    ov = find_range_overlap(a, b)
    if not ov[1]:
        return [a, (0, 0)]
    nov1 = (a[0], ov[0] - a[0])
    if not nov1[1]:
        nov1 = (0, 0)
    nov2 = (ov[0] + ov[1], a[0] + a[1] - ov[0] - ov[1])
    if not nov2[1]:
        nov2 = (0, 0)
    return [nov1, nov2]


def transform(sr, ranges):
    sn = []
    for t in ranges:
        ov = find_range_overlap(sr, (t[1], t[2]))
        if ov[1]:
            sn.append((ov[0] - t[1] + t[0], ov[1]))
            for n in find_non_overlapping(sr, (t[1], t[2])):
                if n[1]:
                    for tran in transform(n, ranges):
                        sn.append(tran)
            return sn
    sn.append(sr)
    return sn


def get_location2(seedlist, almanac):
    i = 1
    sl = seedlist
    while i < len(almanac):
        sn = []
        for s in sl:
            for t in transform(s, almanac[i]):
                sn.append(t)
        sl = sn
        i += 1
    return min(s[0] for s in sl)


def part2(txt):
    m = reader(txt)
    i = 0
    r = []
    while i < len(m[0][0]):
        r.append((m[0][0][i], m[0][0][i + 1]))
        i += 2
    return get_location2(r, m)

