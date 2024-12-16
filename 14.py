from aocd import data
from aocd import submit
import re

W, H = 101, 103

def get_safety_factor(robots):
    n1, n2, n3, n4 = 0, 0, 0, 0

    for x, y, vx, vy in robots:
        if x < W // 2 and y < H // 2:
            n1 += 1
        elif x > W // 2 and y < H // 2:
            n2 += 1
        elif x < W // 2 and y > H // 2:
            n3 += 1
        elif x > W // 2 and y > H // 2:
            n4 += 1

    return n1 * n2 * n3 * n4

def get_var(robots):
    values = list(map(lambda e: e[0] + e[1], robots))
    mean = sum(values) / len(robots)
    return sum(map(lambda v: (v - mean) ** 2, values)) / len(robots)

robots = list(map(lambda e: list(map(int, re.findall(r'-?\d+', e))), data.split('\n')))

min_var = get_var(robots)
part2 = 0

for t in range(1, 10000):
    for r in robots:
        r[0] = (r[0] + r[2]) % W
        r[1] = (r[1] + r[3]) % H

    if (t == 100):
        part1 = get_safety_factor(robots)

    var = get_var(robots)
    if var < min_var:
        min_var = var
        part2 = t

submit(part1, part='a')
submit(part2, part='b')
