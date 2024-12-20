from aocd import data
from aocd import submit
from collections import deque

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

maze = list(map(list, data.split('\n')))

for y, row in enumerate(maze):
    for x, c in enumerate(row):
        if c == 'S':
            sx, sy = x, y
        elif c == 'E':
            ex, ey = x, y

visited = {}
queue = deque()
queue.append((sx, sy, 0, 0, [(sx, sy)]))

score = None
results = {}

while len(queue) > 0:
    x, y, d, s, track = queue.popleft()

    if x == ex and y == ey:
        score = s if score is None else min(s, score)
        if s not in results:
            results[s] = track
        else:
            results[s] += track
        continue

    if score is not None and s > score:
        continue

    if (x, y, d) in visited and visited[(x, y, d)] < s:
        continue

    visited[(x, y, d)] = s

    candidates = []
    for dd in [0, -1, 1, 2]:
        d1 = (d + dd) % len(DIRS)
        x1, y1 = x + DIRS[d1][0], y + DIRS[d1][1]
        s1 = s + 1 + abs(dd) * 1000
        track1 = track + [(x1, y1)]
        candidates.append((x1, y1, d1, s1, track1))
    queue.extend(filter(lambda e: maze[e[1]][e[0]] != '#', candidates))

submit(score, part='a')
submit(len(set(results[score])), part='b')
