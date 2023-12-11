import numpy as np


def reader(txt):
    lines = []
    for line in open(txt):
        lines.append(list(line.replace('\n', '')))
    return lines


def expand(realm):
    depth = []
    for horizontal in realm:
        if all(h == horizontal[0] for h in horizontal):
            depth.append(horizontal)
        depth.append(horizontal)
    expanded = []
    for vertical in np.transpose(depth):
        if all(v == vertical[0] for v in vertical):
            expanded.append(vertical)
        expanded.append(vertical)
    return np.transpose(expanded)


def part1(txt):
    realm = expand(reader(txt))
    galaxies = np.where(np.array(realm) == '#')
    sum = 0
    for i in range(0, len(galaxies[0])):
        for j in range(i + 1, len(galaxies[0])):
            sum += abs(galaxies[0][i] - galaxies[0][j]) + abs(galaxies[1][i] - galaxies[1][j])
    return sum


def get_empty_part(realm):
    hori = []
    for i, horizontal in enumerate(realm):
        if all(h == horizontal[0] for h in horizontal):
            hori.append(i)
    vert = []
    for j, vertical in enumerate(np.transpose(realm)):
        if all(v == vertical[0] for v in vertical):
            vert.append(j)
    return hori, vert


def part2(txt):
    realm = reader(txt)
    empty = get_empty_part(realm)
    galaxies = np.where(np.array(realm) == '#')
    sum = 0
    for i in range(0, len(galaxies[0])):
        for j in range(i + 1, len(galaxies[0])):
            diff = 0
            for h in range(min(galaxies[0][i], galaxies[0][j]), max(galaxies[0][i], galaxies[0][j])):
                if h in empty[0]:
                    diff += 1000000
                else:
                    diff += 1
            for v in range(min(galaxies[1][i], galaxies[1][j]), max(galaxies[1][i], galaxies[1][j])):
                if v in empty[1]:
                    diff += 1000000
                else:
                    diff += 1
            sum += diff
    return sum