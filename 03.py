from aocd import data
from aocd import submit
import re

program = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", data)

sum1 = 0
sum2 = 0
enabled = True

for x, y, do, dont in program:
    if len(x):
        prod = int(x) * int(y)
        sum1 += prod
        sum2 += prod * int(enabled)
    else:
        enabled = bool(do)

submit(sum1, part='a')
submit(sum2, part='b')
