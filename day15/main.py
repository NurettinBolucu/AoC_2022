from helper.helper import FileHelper


def q1(_lines, _row):
    _min_x = min(_lines[0][0], _lines[0][2])
    _max_x = max(_lines[0][0], _lines[0][2])
    for _line in _lines:
        if _min_x > min(_line[0], _line[2]):
            _min_x = min(_line[0], _line[2])
        if _max_x < max(_line[0], _line[2]):
            _max_x = max(_line[0], _line[2])

    _len = int(_max_x - _min_x + 1)
    _map = (['.']*(_len * 3))
    for _line in _lines:
        if _line[1] == _row:
            _map[_line[0] - _min_x + _len] = 'S'
        if _line[3] == _row:
            _map[_line[2] - _min_x + _len] = 'B'

    for _line in _lines:
        distance = abs(_line[2] - _line[0]) + abs(_line[3] - _line[1])
        diff = abs(_line[1] - _row)
        if distance >= diff:
            if _map[_line[0] - _min_x + _len] == '.':
                _map[_line[0] - _min_x + _len] = '#'

            for i in range(distance - diff):
                if _map[_line[0] - _min_x + (i+1) + _len] == '.':
                    _map[_line[0] - _min_x + (i+1) + _len] = '#'
                if _map[_line[0] - _min_x - (i+1) + _len] == '.':
                    _map[_line[0] - _min_x - (i+1) + _len] = '#'

    ctr = 0
    for i in _map:
        if i == '#' or i == 'S':
            ctr = ctr+1

    return ctr


def q2(_lines):
    for _y in range(4000000):    # y
        _x = 0
        while _x < 4000000:    # x
            not_touched = True
            for _line in _lines:
                distance = abs(_line[2] - _line[0]) + abs(_line[3] - _line[1])
                dif = abs(_x - _line[0]) + abs(_y - _line[1])
                if not dif > distance:
                    diff_y = abs(_y - _line[1])
                    diff_x = abs(_x - _line[0])
                    _x += (distance - diff_y) + diff_x + 1
                    not_touched = False

                if _x > 4000000:
                    break

            if not_touched:
                return _y, _x

    return 0, 0


def is_number(n: str) -> bool:
    try:
        int(n)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    file = FileHelper("day15//input.txt")
    glob_lines = file.get_seperated_lines([':', ', ', '='])
    lines = []
    for line in glob_lines:
        lines.append([int(i) for i in line if is_number(i)])

    print("Solution 1: {}".format(q1(lines, 2000000)))
    y, x = q2(lines)
    print("Solution 2: {}".format(x*4000000 + y))
