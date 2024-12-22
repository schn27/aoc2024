from aocd import data
from aocd import submit
from functools import cache

keypad1 = (
    "789",
    "456",
    "123",
    " 0A"
)

keypad2 = (
    " ^A",
    "<v>"
)

def get_moves(keypad):
    xy = {}
    for y, row in enumerate(keypad):
        for x, c in enumerate(row):
            xy[c] = (x, y)

    def get_dx(x1, x2):
        return ('<' if x2 < x1 else '>') * abs(x2 - x1)

    def get_dy(y1, y2):
        return ('^' if y2 < y1 else 'v') * abs(y2 - y1)

    moves = {}

    keys = list(filter(lambda c: c != ' ', list(''.join(keypad))))
    for k1 in keys:
        for k2 in keys:
            seqs = []
            moves[k1 + k2] = seqs
            if k1 == k2:
                seqs.append('A')
            else:
                x1, y1 = xy[k1]
                x2, y2 = xy[k2]
                if x1 == x2:
                    seqs.append(get_dy(y1, y2) + 'A')
                elif y1 == y2:
                    seqs.append(get_dx(x1, x2) + 'A')
                else:
                    if xy[' '] != (x1, y2):
                        seqs.append(get_dy(y1, y2) + get_dx(x1, x2) + 'A')
                    if xy[' '] != (x2, y1):
                        seqs.append(get_dx(x1, x2) + get_dy(y1, y2) + 'A')
    return moves

km = get_moves(keypad1)
km.update(get_moves(keypad2))

@cache
def get_len(code, depth):
    if depth == 0:
        return len(code)

    res = 0

    for e in zip(['A'] + list(code[:-1]), list(code)):
        res += min(get_len(s, depth - 1) for s in km[''.join(e)])

    return res

codes = data.split('\n')
submit(sum(map(lambda c: int(c[:-1]) * get_len(c, 3), codes)), part='a')
submit(sum(map(lambda c: int(c[:-1]) * get_len(c, 26), codes)), part='b')
