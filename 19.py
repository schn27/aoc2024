from aocd import data
from aocd import submit
from functools import cache

patterns, designs = data.split('\n\n')
patterns = patterns.split(', ')
designs = designs.split('\n')

@cache
def get_ways(design):
    if design == "":
        return 1
    return sum(map(lambda p: 0 if not design.startswith(p) else get_ways(design[len(p):]), patterns))

ways = list(map(get_ways, designs))
submit(sum(map(lambda e: 1 if e > 0 else 0, ways)), part='a')
submit(sum(ways), part='b')
