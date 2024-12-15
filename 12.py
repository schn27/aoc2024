from aocd import data
from aocd import submit

neighbours = ((-1, 0), (0, -1), (1, 0), (0, 1))

farm = list(map(list, data.split('\n')))
x_max = len(farm[0])
y_max = len(farm)
visited = set()

def get_region(x, y, c):
    area = []
    wave = [(x, y)]

    while len(wave) > 0:
        x, y = wave.pop()
        if (x, y) not in visited:
            visited.add((x, y))

            fence = []

            for dx, dy in neighbours:
                xx, yy = x + dx, y + dy
                if 0 <= xx < x_max and 0 <= yy < y_max and farm[yy][xx] == c:
                    wave.append((xx, yy))
                else:
                    fence.append((dx, dy))

            area.append((x, y, fence))

    perimeter =0
    fence = {}
    for x, y, f in area:
        if len(f) > 0:
            perimeter += len(f)
            fence_bits = 0
            for b in range(0, len(neighbours)):
                if neighbours[b] in f:
                    fence_bits += 1 << b
            fence[(x, y)] = fence_bits

    def collapse(fence, x, y, dx, dy, mask):
        if fence[(x, y)] & mask:
            x += dx
            y += dy
            while fence.get((x, y), 0) & mask:
                fence[x, y] &= ~mask
                x += dx
                y += dy

    for x, y in fence:
        collapse(fence, x, y, 1, 0, 1 << 1)
        collapse(fence, x, y, 1, 0, 1 << 3)
        collapse(fence, x, y, 0, 1, 1 << 0)
        collapse(fence, x, y, 0, 1, 1 << 2)

    sides = sum(map(lambda v: v.bit_count(), fence.values()))

    return (len(area), perimeter, sides)

regions = []

for y, row in enumerate(farm):
    for x, c in enumerate(row):
        if (x, y) not in visited:
            regions.append(get_region(x, y, c))

submit(sum(map(lambda r: r[0] * r[1], regions)), part='a')
submit(sum(map(lambda r: r[0] * r[2], regions)), part='b')
