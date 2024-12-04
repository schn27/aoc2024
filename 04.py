from aocd import data
from aocd import submit

lines = data.split('\n')

def is_ok_xy(x, y):
    return x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)

def count1():
    count = 0
    word = "XMAS"
    N = len(word) - 1
    dirs = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != word[0]:
                continue

            def is_ok(d):
                return is_ok_xy(x + d[0] * N, y + d[1] * N)

            for d in filter(is_ok, dirs):
                found = True
                for i in range(1, len(word)):
                    xi = x + i * d[0]
                    yi = y + i * d[1]
                    if lines[yi][xi] != word[i]:
                        found = False
                        break
                if found:
                    count += 1
    return count

def count2():
    count = 0
    dirs = ((1, -1), (1, 1), (-1, 1), (-1, -1))

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            def is_ok(d):
                return is_ok_xy(x + d[0], y + d[1])

            if c == 'A' and all(map(is_ok, dirs)):
                ms = ''.join(list(map(lambda d: lines[y + d[1]][x + d[0]], dirs)))
                if ms in ('MSSM', 'MMSS', 'SMMS', 'SSMM'):
                    count += 1

    return count

submit(count1(), part='a')
submit(count2(), part='b')
