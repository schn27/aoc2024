from aocd import data
from aocd import submit
import re

def is_true(test, nums):
    if len(nums) == 1 and test == nums[0]:
        return 1

    ops = [0] * (len(nums))

    while ops[-1] == 0:
        res = nums[0]
        for i, n in enumerate(nums[1:]):
            if ops[i] == 0:
                res *= n
            elif ops[i] == 1:
                res += n
            else:
                res = int(str(res) + str(n))

        if res == test:
            return 2 if any(map(lambda e: e == 2, ops)) else 1

        inc(ops)

    return False

def inc(ops):
    carry = 1
    for i in range(len(ops)):
        ops[i] += carry
        if ops[i] < 3:
            break
        else:
            ops[i] = 0
            carry = 1

equations = map(lambda e: list(map(int, re.findall(r"\d+", e))), data.split('\n'))

count1 = 0
count2 = 0

for e in equations:
    test, nums = e[0], e[1:]
    res = is_true(test, nums)
    if res == 1:
        count1 += test
    elif res == 2:
        count2 += test

submit(count1, part='a')
submit(count1 + count2, part='b')
