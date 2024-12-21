from aocd import data
from aocd import submit
import re

def run(prog, regs):
    regs = regs.copy()
    out = []
    ip = 0

    def get_combo(operand):
        return operand if operand < 4 else regs[operand - 4]

    while ip >= 0 and ip < len(prog) - 1:
        opcode = prog[ip]
        operand = prog[ip + 1]
        new_ip = ip + 2
        if opcode == 0:
            regs[0] = regs[0] // (2 ** get_combo(operand))
        elif opcode == 1:
            regs[1] = regs[1] ^ operand
        elif opcode == 2:
            regs[1] = get_combo(operand) & 7
        elif opcode == 3:
            new_ip = new_ip if regs[0] == 0 else operand
        elif opcode == 4:
            regs[1] = regs[1] ^ regs[2]
        elif opcode == 5:
            out.append(get_combo(operand) & 7)
        elif opcode == 6:
            regs[1] = regs[0] // (2 ** get_combo(operand))
        elif opcode == 7:
            regs[2] = regs[0] // (2 ** get_combo(operand))
        ip = new_ip

    return out

nums = list(map(int, re.findall(r'\d+', data)))
regs = nums[:3]
prog = nums[3:]

submit(','.join(map(str, run(prog, regs))), part='a')

regs[0] = int('1' + '0' * (len(prog) - 1), 8)
i = len(prog) - 1

while i >= 0:
    if (i >= len(prog)):
        raise(Exception('no solution'))

    while True:
        out = run(prog, regs)

        if out[i] == prog[i]:
            i -= 1
            break
        else:
            regs[0] += 8 ** i
            if regs[0] & (7 * 8 ** i) == 0:
                i += 1
                break

submit(regs[0], part='b')
