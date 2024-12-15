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

def get_dist(robots):
    dist = 0

    for i in range(len(robots) // 8 - 1):
        for j in range(i + 1, len(robots) // 8):
            r1, r2 = robots[i], robots[j]
            dist += abs(r1[0] - r2[0]) + abs(r1[1] - r2[1])

    return dist

robots = list(map(lambda e: list(map(int, re.findall(r'-?\d+', e))), data.split('\n')))

min_dist = get_dist(robots)
part2 = 0

for t in range(1, 10000):
    for r in robots:
        r[0] = (r[0] + r[2]) % W
        r[1] = (r[1] + r[3]) % H

    if (t == 100):
        part1 = get_safety_factor(robots)

    dist = get_dist(robots)
    if dist < min_dist:
        min_dist = dist
        part2 = t

submit(part1, part='a')
submit(part2, part='b')
