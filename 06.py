from aocd import data
from aocd import submit

lines = data.split('\n')
x_max = len(lines[0]) - 1
y_max = len(lines) - 1

obstacles = set()
guard = None
dxdy = (0, -1)

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '^':
            guard = (x, y)
        elif c == '#':
            obstacles.add((x, y))

def get_track(guard, dxdy, obstacles, extra=None):
    track = set()

    while (0 <= guard[0] <= x_max and 0 <= guard[1] <= y_max):
        if (guard, dxdy) in track:
            return None
        track.add((guard, dxdy))
        guard1 = (guard[0] + dxdy[0], guard[1] + dxdy[1])
        if guard1 in obstacles or guard1 == extra:
            dxdy = (-dxdy[1], dxdy[0])
        else:
            guard = guard1

    return track

visited = set(map(lambda e: e[0], get_track(guard, dxdy, obstacles)))

def check_extra(xy):
    return xy != guard and get_track(guard, dxdy, obstacles, xy) == None

submit(len(visited), part='a')
submit(len(list(filter(check_extra, visited))), part='b')
