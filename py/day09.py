import regex as re


def reader(txt):
    sets = []
    for line in open(txt):
        sets.append(list(map(int, line.split())))
    return sets


def calc_next(seq):
    if all(nums == seq[0] for nums in seq):
        return seq[0]
    diff = []
    i = 0
    while i < len(seq) - 1:
        diff.append(seq[i + 1] - seq[i])
        i += 1
    return seq[-1] + calc_next(diff)


def part1(txt):
    sets = reader(txt)
    solution = 0
    for s in sets:
        solution += calc_next(s)
    return solution


def part2(txt):
    sets = reader(txt)
    solution = 0
    for s in sets:
        s.reverse()
        solution += calc_next(s)
    return solution

