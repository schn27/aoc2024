from aocd import data
from aocd import submit
import re

def solve(ax, ay, bx, by, x, y):
    a = round((x / bx - y / by) / (ax / bx - ay / by))
    b = round((x / ax - y / ay) / (bx / ax - by / ay))
    if a >= 0 and b >= 0 and (ax * a + bx * b == x) and (ay * a + by * b == y):
        return a * 3 + b
    else:
        return 0

cases = map(lambda e: map(int, re.findall(r'\d+', e)), data.split('\n\n'))

tokens1 = 0
tokens2 = 0
ERROR = 10000000000000

for ax, ay, bx, by, x, y in cases:
    tokens1 += solve(ax, ay, bx, by, x, y)
    tokens2 += solve(ax, ay, bx, by, x + ERROR, y + ERROR)

submit(tokens1, part='a')
submit(tokens2, part='b')
