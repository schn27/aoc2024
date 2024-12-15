from aocd import data
from aocd import submit
from functools import cache
import re

def blink(stone):
    if stone == 0:
        return (1, None)

    s = str(stone)
    n = len(s)

    if n % 2 == 1:
        return (stone * 2024, None)

    return (int(s[:n // 2]), int(s[n // 2:]))

@cache
def get_stones_after(stone, blinks):
    count = 1

    for b in range(blinks, 0, -1):
        stone, new_stone = blink(stone)
        if new_stone is not None:
            count += get_stones_after(new_stone, b - 1)

    return count

stones = list(map(int, re.findall(r'\d+', data)))
submit(sum(map(lambda s: get_stones_after(s, 25), stones)), part='a')
submit(sum(map(lambda s: get_stones_after(s, 75), stones)), part='b')
