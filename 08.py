from aocd import data
from aocd import submit

lines = data.split('\n')
x_max = len(lines[0])
y_max = len(lines)

antennas = {}

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != '.':
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((x, y))

antinodes = set()
antinodes2 = set([e for a in antennas.values() for e in a])

def is_in_bounds(xy):
    return 0 <= xy[0] < x_max and 0 <= xy[1] < y_max

def add_antinodes(a, d):
    for i in range(1, max(x_max, y_max)):
        c = (a[0] + i * d[0], a[1] + i * d[1])
        if not is_in_bounds(c):
            break

        if i == 1:
            antinodes.add(c)

        antinodes2.add(c)

for f in antennas:
    for i, a in enumerate(antennas[f][:-1]):
        for b in antennas[f][i + 1:]:
            d = (a[0] - b[0], a[1] - b[1])
            add_antinodes(a, d)
            add_antinodes(b, (-d[0], -d[1]))

submit(len(antinodes), part='a')
submit(len(antinodes2), part='b')
