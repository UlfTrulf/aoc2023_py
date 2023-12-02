import regex as re


num_dict = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}


def get_f_l(array):
    return [num_dict.get(array[0], array[0]), num_dict.get(array[-1], array[-1])]


def part1(txt):
    f = open(txt)
    s = 0
    for line in f:
        s += int(''.join(map(str, get_f_l(re.findall(r'\d', line)))))
    return s


def part2(txt):
    f = open(txt)
    s = 0
    numbers = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    for line in f:
        s += int(''.join(map(str, get_f_l(re.findall(numbers, line)))))
    return s
