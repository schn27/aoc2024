from aocd import data
from aocd import submit

def next(v):
    v ^= v * 64
    v %= 16777216
    v ^= v // 32
    v ^= v * 2048
    v %= 16777216
    return v

def get_secrets(v):
    res = []
    for i in range(2000):
        v = next(v)
        res.append(v)
    return res

nums = list(map(int, data.split('\n')))
secrets = list(map(get_secrets, nums))
submit(sum(map(lambda s: s[-1], secrets)), part='a')

prices = list(map(lambda s: list(map(lambda v: v % 10, s)), secrets))
diffs = list(map(lambda p: list(map(lambda e: e[1] - e[0], zip(p[:-1], p[1:]))), prices))

seqs = {}

for p, d in zip(prices, diffs):
    seq = {}
    for i, e in enumerate(zip(d[:-3], d[1:-2], d[2:-1], d[3:])):
        if e not in seq:
            seq[e] = p[i + 4]
    for e in seq:
        seqs[e] = seq[e] + (seqs[e] if e in seqs else 0)

submit(max(seqs.values()), part='b')
