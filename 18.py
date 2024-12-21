from aocd import data
from aocd import submit

START = (0, 0)
GOAL = (70, 70)
corrupted = set()

def get_path():
    visited = set()
    step = 0
    front = set([START])

    while True:
        if len(front) == 0:
            return None

        if GOAL in front:
            break

        visited.update(front)
        new_front = set()
        for x, y in front:
            candidats = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            candidats = filter(lambda e: 0 <= e[0] <= GOAL[0] and 0 <= e[1] <= GOAL[1]
                and e not in corrupted and e not in visited, candidats)
            new_front.update(candidats)
        front = new_front
        step += 1

    return step

pos = map(lambda e: tuple(map(int, e.split(','))), data.split('\n'))
for i, p in enumerate(pos):
    corrupted.add(p)
    if i == 1023:
        part1 = get_path()
    elif i > 1023 and get_path() is None:
        part2 = ','.join(map(str, p))
        break

submit(part1, part='a')
submit(part2, part='b')
