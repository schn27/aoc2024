from aocd import data
from aocd import submit

layout = list(map(int, [*data]))

def get_disk(layout):
    files = []
    frees = []
    file_id = 0
    file = True
    pos = 0

    for e in layout:
        if file:
            files.append([pos, e, file_id])
            file_id += 1
        elif e > 0:
            frees.append([pos, e, -1])

        pos += e
        file = not file

    return [files, frees]

def get_flat_disk(disk):
    files, frees = disk
    disk = []
    for e in sorted([*files, *frees], key=lambda e: e[0]):
        disk.extend([e[2]] * e[1])
    return disk

def rearange(disk):
    disk = get_flat_disk(disk)
    free_index = 0
    file_index = len(disk) - 1

    while (free_index < file_index):
        while disk[free_index] != -1 and free_index < len(disk):
            free_index += 1
        while disk[file_index] == -1 and file_index >= 0:
            file_index -= 1
        if free_index >= len(disk) or file_index < 0 or free_index > file_index:
            break
        disk[free_index], disk[file_index] = disk[file_index], disk[free_index]
        free_index += 1
        file_index -= 1

    return disk

def rearange2(disk):
    files, frees = disk
    files = files[::-1]

    for file in files:
        frees = sorted(frees, key=lambda e: e[0])
        for free in frees:
            if free[0] > file[0]:
                break

            if file[1] == free[1]:
                file[0], free[0] = free[0], file[0]
                break
            elif file[1] <= free[1]:
                free_pos = free[0]
                file_pos = file[0]
                file[0] = free_pos
                free[0] += file[1]
                free[1] -= file[1]
                frees.append([file_pos, file[1], -1])
                break

    return get_flat_disk([files, frees])

def get_checksum(disk):
    return sum([i * max(e, 0) for i, e in enumerate(disk)])

disk = get_disk(layout)
submit(get_checksum(rearange(disk)), part='a')
submit(get_checksum(rearange2(disk)), part='b')
