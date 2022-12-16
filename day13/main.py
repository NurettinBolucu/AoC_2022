from helper.helper import FileHelper
import functools


def check_pair(line_1, line_2):
    for i in range(min(len(line_1), len(line_2))):
        if isinstance(line_1[i], int) and isinstance(line_2[i], int):
            if line_1[i] < line_2[i]:
                return True
            elif line_1[i] > line_2[i]:
                return False
        elif isinstance(line_1[i], list) and isinstance(line_2[i], list):
            temp = check_pair(line_1[i], line_2[i])
            if temp is None:
                continue
            else:
                return temp
        else:
            if isinstance(line_1[i], int):
                temp = check_pair([line_1[i]], line_2[i])
                if temp is None:
                    continue
                else:
                    return temp
            else:
                temp = check_pair(line_1[i], [line_2[i]])
                if temp is None:
                    continue
                else:
                    return temp

    if len(line_1) == len(line_2):
        return None

    if len(line_1) < len(line_2):
        return True
    else:
        return False

    pass


def parse_input(lines):

    pairs = []
    for i in range(int(len(lines)/3)+1):
        for j in range(2):
            line = lines[i*3+j]
            pairs.append(eval(line))

    return pairs


def q1(pairs):
    ctr = 0
    total = 0

    for i in range(0, len(pairs), 2):
        ctr += 1
        if check_pair(pairs[i], pairs[i+1]):
            total += ctr
    return total


def sort_tool(left, right):
    temp = check_pair(left, right)
    if temp is None:
        return 0
    elif temp is True:
        return -1
    else:
        return 1


def q2(pairs):
    pairs.append([[2]])
    pairs.append([[6]])
    s = sorted(pairs, key=functools.cmp_to_key(sort_tool))
    return (s.index([[2]]) + 1) * (s.index([[6]]) + 1)


if __name__ == "__main__":
    file = FileHelper("day13//input.txt")
    glob_lines = file.get_lines()

    solution = q1(parse_input(glob_lines))
    print("Solution 1: {}".format(solution))

    solution = q2(parse_input(glob_lines))
    print("Solution 2: {}".format(solution))
