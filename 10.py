from aocd import data
from aocd import submit
from collections import deque

m = list(map(lambda e: list(map(int, list(e))), data.split('\n')))
x_max = len(m[0])
y_max = len(m)

def is_in_bounds(xy):
    x, y = xy
    return 0 <= x < x_max and 0 <= y < y_max

def get(xy):
    return m[xy[1]][xy[0]]

def get_score_rating(xy):
    wave = deque([xy])
    reached = set()
    rating = 0

    while len(wave) > 0:
        xy = wave.popleft()
        if get(xy) == 9:
            reached.add(xy)
            rating += 1
        else:
            x, y = xy
            candidats = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            candidats = filter(lambda e: is_in_bounds(e) and get(e) - get(xy) == 1, candidats)
            for c in candidats:
                wave.append(c)

    return len(reached), rating

part1 = 0
part2 = 0

for y, r in enumerate(m):
    for x, c in enumerate(r):
        if c == 0:
            score, rating = get_score_rating((x, y))
            part1 += score
            part2 += rating

submit(part1, part='a')
submit(part2, part='b')
