from aocd import data
from aocd import submit
import re

memo = {}

def get_stones_after(stone, blinks):
    key = (stone, blinks)

    if key not in memo:
        count = 1

        for b in range(blinks, 0, -1):
            if stone == 0:
                stone = 1
            else:
                str_s = str(stone)
                len_s = len(str_s)
                if len_s & 1 == 1:
                    stone *= 2024
                else:
                    stone = int(str_s[:len_s // 2])
                    count += get_stones_after(int(str_s[len_s // 2:]), b - 1)

        memo[key] = count

    return memo[key]

stones = list(map(int, re.findall(r'\d+', data)))
submit(sum(map(lambda s: get_stones_after(s, 25), stones)), part='a')
submit(sum(map(lambda s: get_stones_after(s, 75), stones)), part='b')
