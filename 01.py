from aocd import data
from aocd import submit

lists = map(lambda line: map(int, line.split()), data.split('\n'))
left, right = map(sorted, map(list, zip(*lists)))
submit(sum(map(lambda e: abs(e[0] - e[1]), zip(left, right))), part='a')
submit(sum(map(lambda e: e * right.count(e), left)), part='b')

