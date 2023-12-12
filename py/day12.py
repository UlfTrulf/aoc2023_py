import regex as re
from functools import cache


def reader(txt):
    groups = []
    for line in open(txt):
        groups.append((line.split()[0], list(map(int, re.findall(r'\d+', line.split()[1])))))
    return groups


def generate_substrings(base_s, num_hash):
    substrings = [base_s]
    for i in range(base_s.count('?')):
        sub = []
        for s in substrings:
            a = s.replace('?', '#', 1)
            if a.count('#') <= num_hash <= a.count('#') + a.count('?'):
                sub.append(a)
            a = s.replace('?', '.', 1)
            if a.count('#') <= num_hash <= a.count('#') + a.count('?'):
                sub.append(a)
        substrings = sub
    return substrings


def part1(txt):
    count = 0
    for g in reader(txt):
        pattern = re.compile('(.*)' + '(.+)'.join(['#'*i for i in g[1]]) + '(.*)')
        substrings = generate_substrings(g[0], sum(g[1]))
        valid = [s for s in substrings if re.match(pattern, s)]
        count += len(valid)
    return count


@cache
def get_combinations(string, blocks, count=None):
    if count is None or count == 0:
        if not(string.count('#') + string.count('?') >= sum(blocks) >= string.count('#')):
            return 0
    if len(blocks) == 0 and count is None:
        return string.count('#') == 0

    if string[:1] == '' and (not count or count == 0):
        return len(blocks) == 0
    elif string[:1] == '' and count:
        return 0

    elif string[:1] == '.' and (not count or count == 0):
        return get_combinations(string[1:], blocks)
    elif string[:1] == '.' and count != 0:
        return 0

    elif string[:1] == '?' and count == 0:
        return get_combinations(string[1:], blocks)
    elif string[:1] == '?' and count is None:
        dont = get_combinations(string[1:], blocks)
        do = get_combinations(string[1:], blocks[1:], blocks[0] - 1)
        return do + dont
    elif string[:1] == '?':
        return get_combinations(string[1:], blocks, count - 1)

    elif string[:1] == '#' and count == 0:
        return 0
    elif string[:1] == '#' and count is None:
        return get_combinations(string[1:], blocks[1:], blocks[0] - 1)
    elif string[:1] == '#':
        return get_combinations(string[1:], blocks, count - 1)


def part2(txt):
    count = 0
    for i, g in enumerate(reader(txt)):
        count += get_combinations('?'.join([g[0]] * 5), tuple(g[1] * 5))
    return count
