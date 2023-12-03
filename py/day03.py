import numpy as np
import regex as re


def reader(txt, reg):
    num = []
    sym = []
    for line in open(txt):
        numbers = re.findall(r'\d+', line)
        indices_num = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        num.append([numbers, indices_num])
        indices_sym = [(m.start(0)) for m in re.finditer(reg, line)]
        sym.append(indices_sym)
    return num, sym


def part1(txt):
    s = 0
    num, sym = reader(txt, r'[^\d\.\n]')
    i = 0
    while i < len(sym):
        for sy in sym[i]:
            k = -1
            while k < 2:
                if len(sym) >= i + k >= 0:
                    mi = [j for j, t in enumerate(num[i + k][1]) if sy in range(t[0]-1, t[1]+1)]
                    for m in mi:
                        s += int(num[i + k][0][m])
                k += 1
        i += 1
    return s


def part2(txt):
    s = 0
    num, sym = reader(txt, r'\*')
    i = 0
    while i < len(sym):
        for sy in sym[i]:
            k = -1
            m = []
            while k < 2:
                if len(sym) >= i + k >= 0:
                    mi = [j for j, t in enumerate(num[i + k][1]) if sy in range(t[0] - 1, t[1] + 1)]
                    for ma in mi:
                        m.append(int(num[i + k][0][ma]))
                k += 1
            if len(m) == 2:
                s += np.prod(m)
        i += 1
    return s
