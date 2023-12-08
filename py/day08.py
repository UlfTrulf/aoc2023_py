import regex as re
import math


def reader(txt):
    with open(txt) as file:
        content = file.read().split('\n\n')
    lines = content[1].split('\n')
    instructions = []
    for ins in lines:
        instructions.append(re.split(r'=|,', ins.replace(' ', '')
                            .replace('(', '')
                            .replace(')', '')))
    return content[0].replace('L', '1').replace('R', '2'), instructions


def part1(txt):
    current = 'AAA'
    order, instructions = reader(txt)
    i = 0
    while current != 'ZZZ':
        side = int(order[i % len(order)])
        for x in instructions:
            if x[0] == current:
                current = x[side]
                break

        i += 1
    return i


def part2(txt):
    order, instructions = reader(txt)
    currents = []
    for ins in instructions:
        if ins[0][2] == 'A':
            currents.append(ins[0])
    loops = []
    for current in currents:
        c = current
        i = 0
        looped = False
        while not looped:
            side = int(order[i % len(order)])
            for x in instructions:
                if x[0] == c:
                    if c[2] == 'Z':
                        loops.append(i)
                        looped = True
                    c = x[side]
                    break
            i += 1
    return math.lcm(*loops)
