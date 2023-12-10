direction_dict = {
    ('-', (0, 1)): (0, 1),
    ('-', (0, -1)): (0, -1),
    ('|', (1, 0)): (1, 0),
    ('|', (-1, 0)): (-1, 0),
    ('L', (1, 0)): (0, 1),
    ('L', (0, -1)): (-1, 0),
    ('J', (1, 0)): (0, -1),
    ('J', (0, 1)): (-1, 0),
    ('7', (0, 1)): (1, 0),
    ('7', (-1, 0)): (0, -1),
    ('F', (0, -1)): (1, 0),
    ('F', (-1, 0)): (0, 1),
}


def reader(txt):
    vert = []
    for line in open(txt):
        vert.append([c for c in line])
    return vert


def find_char(c, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == c:
                return i, j


def fist_step(start, area):
    up = area[start[0] - 1][start[1]]
    if up == 'F' or up == '7' or up == '|':
        print(area[start[0] - 1][start[1]])
        return -1, 0
    right = area[start[0]][start[1] + 1]
    if right == 'J' or right == '7' or right == '-':
        return 0, 1
    down = area[start[0] + 1][start[1]]
    if down == 'J' or down == 'L' or down == '|':
        return 1, 0
    left = area[start[0]][start[1] - 1]
    if left == 'F' or left == 'L' or left == '-':
        return 0, -1


def part1(txt):
    pipes = reader(txt)
    start = find_char('S', pipes)
    step = fist_step(start, pipes)
    position = tuple(map(sum, zip(start, step)))
    current = (pipes[position[0]][position[1]], step)
    count = 1
    while current[0] != 'S':
        step = direction_dict.get(current)
        position = tuple(map(sum, zip(position, step)))
        current = (pipes[position[0]][position[1]], step)
        count += 1
    return round(count / 2)


def part2(txt):
    pipes = reader(txt)
    start = find_char('S', pipes)
    step = fist_step(start, pipes)
    position = tuple(map(sum, zip(start, step)))
    current = (pipes[position[0]][position[1]], step)
    visited = set()
    visited.add(position)
    prev_pos = position
    area = (start[0] - position[0]) * (start[1] + position[1])
    count = 0
    while current[0] != 'S':
        step = direction_dict.get(current)
        position = tuple(map(sum, zip(prev_pos, step)))
        visited.add(position)
        area += (prev_pos[0] - position[0]) * (prev_pos[1] + position[1])
        count += 1
        current = (pipes[position[0]][position[1]], step)
        prev_pos = position
    return abs(area) // 2 - count // 2

