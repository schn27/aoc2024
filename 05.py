from aocd import data
from aocd import submit
from functools import cmp_to_key

section1, section2 = data.split('\n\n')

rules = {}
for e in section1.split('\n'):
    a, b = map(int, e.split('|'))
    if a not in rules:
        rules[a] = set()
    rules[a].add(b)

updates = map(lambda e: list(map(int, e.split(','))), section2.split('\n'))

count1 = 0
count2 = 0

def is_in_order(pair):
    a, b = pair
    return b not in rules or a not in rules[b]

def compare(a, b):
    return 1 if is_in_order((a, b)) else -1

for u in updates:
    if all(map(is_in_order, zip(u[:-1], u[1:]))):
        count1 += u[len(u) // 2]
    else:
        corrected = sorted(u, key=cmp_to_key(compare))
        count2 += corrected[len(corrected) // 2]

submit(count1, part='a')
submit(count2, part='b')
