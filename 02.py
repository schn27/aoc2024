from aocd import data
from aocd import submit

reports = map(lambda line: list(map(int, line.split())), data.split('\n'))

safe = 0
safe2 = 0

def is_safe(r):
    diff = [x - r[i] for i, x in enumerate(r[1:])]
    return all(map(lambda e: abs(e) >= 1 and abs(e) <= 3 and e * diff[0] > 0, diff))

for r in reports:
    if is_safe(r):
        safe += 1
    elif any(map(lambda i: is_safe(r[:i] + r[i + 1:]), range(len(r)))):
        safe2 += 1

submit(safe, part='a')
submit(safe + safe2, part='b')


