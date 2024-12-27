from aocd import data
from aocd import submit

values, gates = data.split('\n\n')
values = {k:int(v) for k, v in map(lambda e: e.split(': '), values.split('\n'))}
gates = {c:(op, a, b) for a, op, b, _, c in map(lambda e: e.split(' '), gates.split('\n'))}
gates_inv = {gates[c]:c for c in gates}

def get(c):
    if c in values:
        return values[c]

    op, a, b = gates[c]
    va = get(a)
    vb = get(b)

    if op == 'AND':
        vc = va & vb
    elif op == 'OR':
        vc = va | vb
    elif op == 'XOR':
        vc = va ^ vb

    values[c] = vc
    return vc

zs = []

for z in sorted(filter(lambda e: e[0] == 'z', gates.keys())):
    zs.append(get(z))

submit(int(''.join(map(str, zs[::-1])), 2), part='a')

"""
1-bit adder

the first bit (no carry from the previous adder)
            ___
x0 ---o-x0-|XOR|-z0
y0 -o-+-y0-|___|
    | |     ___
    | +-x0-|AND|-c0
    +---y0-|___|

other bits

ci-1 ----------------+       ___
              ___    o----c-|XOR|-zi---------- zi
  xi ---o-xi-|XOR|-u-+-o--u-|___|
  yi -o-+-yi-|___|   | |     ___         ___
      | |            | +--u-|AND|-v---v-|OR |- ci (zi+1 for the last bit)
      | |            +----c-|___|   +-w-|___|
      | |                    ___    |
      | +----------------xi-|AND|-w-+
      +------------------yi-|___|

"""

def get_out_for(op, a, b):
    if (op, a, b) in gates_inv:
        return gates_inv[(op, a, b)]
    if (op, b, a) in gates_inv:
        return gates_inv[(op, b, a)]
    return None

wrong = []

def swap_gates(a, b):
    wrong.extend([a, b])
    gates[a], gates[b] = gates[b], gates[a]
    global gates_inv
    gates_inv = {gates[c]:c for c in gates}
    return b, a

n = int(sorted(filter(lambda e: e[0] == 'x', values.keys()))[-1][1:])

c = None

for i in range(n + 1):
    if i == 0:
        u = get_out_for('XOR', f'x{i:02}', f'y{i:02}')

        if u != f'z{i:02}':
            swap_gates(u, f'z{i:02}')

        c = get_out_for('AND', f'x{i:02}', f'y{i:02}')
    else:
        u = get_out_for('XOR', f'x{i:02}', f'y{i:02}')
        z = get_out_for('XOR', u, c)
        v = get_out_for('AND', u, c)

        if z is None or v is None:
            op, a, b = gates[f'z{i:02}']

            if c in [a, b]:
                u, _ = swap_gates(u, b if a == c else a)
            else:
                c, _ = swap_gates(c, b if a == u else a)

            z = get_out_for('XOR', u, c)
            v = get_out_for('AND', u, c)

        elif z != f'z{i:02}':
            swap_gates(z, f'z{i:02}')
            v = get_out_for('AND', u, c)

        w = get_out_for('AND', f'x{i:02}', f'y{i:02}')
        c = get_out_for('OR', v, w)

        if i == n and c != f'z{i+1:02}':
            swap_gates(c, f'z{i+1:02}')

submit(','.join(sorted(wrong)), part='b')
