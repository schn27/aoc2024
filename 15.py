from aocd import data
from aocd import submit
import re

DIRS = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

warehouse, moves = data.split('\n\n')
moves = list(''.join(moves.split('\n')))

walls = set()
boxes = set()
robot = None

walls2 = set()
boxes2 = set()
robot2 = None

for y, row in enumerate(warehouse.split('\n')):
    for x, c in enumerate(row):
        if c == '#':
            walls.add((x, y))
            walls2.add((x * 2, y))
            walls2.add((x * 2 + 1, y))
        elif c == 'O':
            boxes.add((x, y))
            boxes2.add((x * 2, y))
        elif c == '@':
            robot = (x, y)
            robot2 = (x * 2, y)

def get_moving_boxes_a(walls, boxes, xy, dxdy):
    if xy in walls:
        return None
    if xy not in boxes:
        return []
    moving = get_moving_boxes_a(walls, boxes, (xy[0] + dxdy[0], xy[1] + dxdy[1]), dxdy)
    return None if moving is None else [xy] + moving

def get_moving_boxes_b(walls, boxes, xy, dxdy):
    if xy in walls:
        return None

    if dxdy[0] != 0:
        xy = xy if dxdy[0] > 0 else (xy[0] - 1, xy[1])
        if xy not in boxes:
            return []
        moving = get_moving_boxes_b(walls, boxes, (xy[0] + (-1 if dxdy[0] == -1 else 2), xy[1]), dxdy)
        return None if moving is None else [xy] + moving
    else:
        xy2 = (xy[0] - 1, xy[1])
        if xy not in boxes and xy2 not in boxes:
            return []
        if xy not in boxes:
            xy = xy2

        moving1 = get_moving_boxes_b(walls, boxes, (xy[0], xy[1] + dxdy[1]), dxdy)
        moving2 = get_moving_boxes_b(walls, boxes, (xy[0] + 1, xy[1] + dxdy[1]), dxdy)
        return None if moving1 is None or moving2 is None else [xy] + moving1 + moving2

def do_moves(moves, robot, walls, boxes, part='a'):
    boxes = boxes.copy()

    get_moving_boxes = get_moving_boxes_a if part == 'a' else get_moving_boxes_b

    for m in moves:
        dxdy = DIRS[m]
        new_robot = (robot[0] + dxdy[0], robot[1] + dxdy[1])
        moving = get_moving_boxes(walls, boxes, new_robot, dxdy)
        if moving is not None:
            robot = new_robot
            moving = set(moving)
            for b in moving:
                boxes.remove(b)
            for b in moving:
                boxes.add((b[0] + dxdy[0], b[1] + dxdy[1]))

    return boxes

def get_gps_sum(boxes):
    return sum(map(lambda e: e[0] + 100 * e[1], boxes))

submit(get_gps_sum(do_moves(moves, robot, walls, boxes)), part='a')
submit(get_gps_sum(do_moves(moves, robot2, walls2, boxes2, 'b')), part='b')
