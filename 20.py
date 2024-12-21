from aocd import data
from aocd import submit

walls = set()
start = None
end = None

rows = data.split('\n')
width = len(rows[0])
height = len(rows)

for y, row in enumerate(rows):
    for x, c in enumerate(row):
        if c == 'S':
            start = (x, y)
        elif c == 'E':
            end = (x, y)
        elif c == '#':
            walls.add((x, y))

def get_wave():
    wave = {}
    step = 0
    front = set([end])

    while True:
        if len(front) == 0:
            return None

        for e in front:
            wave[e] = step

        if start in front:
            break

        new_front = set()
        for x, y in front:
            candidats = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            candidats = filter(lambda e: 0 <= e[0] <= width and 0 <= e[1] <= height
                and e not in walls and e not in wave, candidats)
            new_front.update(candidats)
        front = new_front
        step += 1

    return wave

def get_cheat(n):
    if n < 2:
        return None

    res = set()
    x, y = -n, 0
    dx, dy = 1, -1

    while (x, y) not in res:
        res.add((x, y))
        x, y = x + dx, y + dy
        if x == 0 or y == 0:
            dx, dy = -dy, dx

    return res

wave = get_wave()
cheats = [get_cheat(i) for i in range(21)]

part1 = 0
part2 = 0

for x, y in wave:
    for i in range(2, 21):
        candidats = map(lambda e: (x + e[0], y + e[1]), cheats[i])
        n = len(list(filter(lambda e: e in wave and wave[(x, y)] - wave[e] - i >= 100, candidats)))
        if i == 2:
            part1 += n
        part2 += n

submit(part1, part='a')
submit(part2, part='b')
