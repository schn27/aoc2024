from aocd import data
from aocd import submit
import re

DIRS = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

warehouse, moves = data.split('\n\n')
warehouse = list(map(list, warehouse.split('\n')))
moves = list(''.join(moves.split('\n')))

def get_moving(warehouse, x, y, dx, dy):
    c = warehouse[y][x]

    if c == '#':
        return None
    if c == '.':
        return []
    if c == 'O' or dx != 0:
        moving = get_moving(warehouse, x + dx, y + dy, dx, dy)
        return None if moving is None else [(x, y, c)] + moving

    side = 1 if c == '[' else -1
    c2 = warehouse[y][x + side]

    moving1 = get_moving(warehouse, x + dx, y + dy, dx, dy)
    moving2 = get_moving(warehouse, x + dx + side, y + dy, dx, dy)
    return None if moving1 is None or moving2 is None else [(x, y, c), (x + side, y, c2)] + moving1 + moving2

def do_moves(warehouse, robot):
    x, y = robot

    for m in moves:
        dx, dy = DIRS[m]
        x1, y1 = x + dx, y + dy
        moving = get_moving(warehouse, x1, y1, dx, dy)
        if moving is None:
            continue
        x, y = x1, y1
        for bx, by, c in moving:
            warehouse[by][bx] = '.'
        for bx, by, c in moving:
            warehouse[by + dy][bx + dx] = c

    return warehouse

def get_gps_sum(warehouse):
    res = 0

    for y, row in enumerate(warehouse):
        for x, c in enumerate(row):
            if c == 'O' or c == '[':
                res += x + 100 * y
    return res

warehouse2 = []

for y, row in enumerate(warehouse):
    row2 = []
    for x, c in enumerate(row):
        if c in ['#', '.']:
            row2 += [c] * 2
        elif c == 'O':
            row2 += ['[', ']']
        elif c == '@':
            warehouse[y][x] = '.'
            robot = (x, y)
            row2 += ['.', '.']
            robot2 = (x * 2, y)
    warehouse2.append(row2)

submit(get_gps_sum(do_moves(warehouse, robot)), part='a')
submit(get_gps_sum(do_moves(warehouse2, robot2)), part='b')
