from helper.helper import FileHelper
import functools


def q1(_sand_map):
    ctr = 0
    while True:
        _start = [0, 500]
        updated = True
        while True:
            if _start[0]+1 == 500:
                updated = False
                break
            try:
                if _sand_map[_start[0]+1][_start[1]] == 0:
                    _start = [_start[0]+1, _start[1]]
                elif _sand_map[_start[0]+1][_start[1]-1] == 0:
                    _start = [_start[0]+1, _start[1]-1]
                elif _sand_map[_start[0]+1][_start[1]+1] == 0:
                    _start = [_start[0]+1, _start[1]+1]
                else:
                    _sand_map[_start[0]][_start[1]] = 1
                    break
            except:
                raise RuntimeError("Fialed {}".format(_start))

        if not updated:
            break
        else:
            ctr += 1

    return ctr


def q2(_sand_map):
    highest = 0
    for i in range(500-1, -1, -1):
        highest = i
        if sum(_sand_map[i]) != 0:
            break

    _sand_map[highest+2] = [1] * 1000
    ctr = 0
    while True:
        _start = [0, 500]
        updated = False
        while True:
            if _sand_map[_start[0]+1][_start[1]] == 0:
                _start = [_start[0]+1, _start[1]]
                updated = True
            elif _sand_map[_start[0]+1][_start[1]-1] == 0:
                _start = [_start[0]+1, _start[1]-1]
                updated = True
            elif _sand_map[_start[0]+1][_start[1]+1] == 0:
                _start = [_start[0]+1, _start[1]+1]
                updated = True
            else:
                _sand_map[_start[0]][_start[1]] = 1
                break

        if not updated:
            break
        else:
            ctr += 1

    return ctr+1


def create_map(_lines):
    _sand_map = []
    for i in range(500):
        _sand_map.append([0] * 1000)

    for line in lines:
        for i in range(len(line) - 1):
            point_1 = eval(line[i])
            point_2 = eval(line[i+1])
            if point_1[0] == point_2[0]:
                _start = min(point_1[1], point_2[1])
                _end = max(point_1[1], point_2[1])
                for j in range(_end - _start + 1):
                    _sand_map[j+_start][point_1[0]] = 1
            else:
                _start = min(point_1[0], point_2[0])
                _end = max(point_1[0], point_2[0])
                for j in range(_end - _start + 1):
                    _sand_map[point_1[1]][j+_start] = 1

    return _sand_map


if __name__ == "__main__":
    file = FileHelper("day14//input.txt")
    glob_lines = file.get_lines()
    lines = [(i.strip().split(" -> ")) for i in glob_lines]
    sand_map = create_map(lines)

    print("Solution 1: {}".format(q1(create_map(glob_lines))))
    print("Solution 2: {}".format(q2(create_map(glob_lines))))
