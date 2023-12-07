from collections import Counter


def reader(txt, prio, p2):
    cards = []
    rank_dict = {char: c for c, char in enumerate(prio)}
    for line in open(txt):
        l = line.replace('\n', '').split(' ')
        c = []
        for card in l[0]:
            c.append(rank_dict.get(card))
        if p2:
            jackless = l[0].replace('J', '')
            jack_count = 5 - len(jackless)
            type = check_type(jackless)
            while jack_count > 0:
                if 6 > type > 2:
                    type -= 2
                else:
                    type -= 1
                jack_count -= 1
        else:
            type = check_type(l[0])
        cards.append((type, c,  int(l[1])))
    return cards


def check_type(cards):
    counted = Counter(cards).most_common()
    if len(counted) == 0:
        return 7
    if len(counted) > 1:
        if counted[0][1] == 3 and counted[1][1] == 2:
            return 2
        elif counted[0][1] == 2 and counted[1][1] == 2:
            return 4
    if counted[0][1] == 5:
        return 0
    elif counted[0][1] == 4:
        return 1
    elif counted[0][1] == 3:
        return 3
    elif counted[0][1] == 2:
        return 5
    else:
        return 6


def calc_sum(cards):
    sorted_cards = sorted(cards, reverse=True)
    sum = 0
    i = 1
    while i <= len(sorted_cards):
        sum += i * sorted_cards[i - 1][2]
        i += 1
    return sum


def part1(txt):
    prio = 'AKQJT98765432'
    return calc_sum(reader(txt, prio, False))


def part2(txt):
    prio = 'AKQT98765432J'
    return calc_sum(reader(txt, prio, True))

