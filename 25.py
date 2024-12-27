from aocd import data
from aocd import submit

def parse(img):
    return list(map(lambda e: int(e.replace('.', '0').replace('#', '1'), 2), img.split('\n')))

images = list(map(parse, data.split('\n\n')))

pairs = 0

for i, u in enumerate(images[:-1]):
    for v in images[i+1:]:
        if all(map(lambda e: (e[0] & e[1]) == 0, zip(u, v))):
            pairs += 1

submit(pairs, part='a')
