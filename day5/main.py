from helper.helper import FileHelper
from copy import deepcopy


def create_stack(lines):
    stc = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(8):
            if lines[7-j][1 + i*4] != ' ':
                stc[i].append(lines[7-j][1 + i*4])

    return stc


def q1(fl, lines, stc):
    for i in range(len(lines) - 10):
        line = fl.split_line(lines[i+10], ' ')
        for s in range(int(line[1])):
            t = stc[int(line[3])-1].pop()
            stc[int(line[5])-1].append(t)

    retVal = ''
    for i in stc:
        retVal += i[len(i) - 1]
    return retVal


def q2(fl, lines, stc):
    for i in range(len(lines) - 10):
        line = fl.split_line(lines[i+10], ' ')
        t = []
        for s in range(int(line[1])):
            t.append(stc[int(line[3])-1].pop())
        for s in range(int(line[1])):
            stc[int(line[5])-1].append(t.pop())

    retVal = ''
    for i in stc:
        retVal += i[len(i) - 1]
    return retVal


if __name__ == "__main__":
    file = FileHelper("day5//input.txt")
    glob_lines = file.get_lines()
    stack_1 = create_stack(glob_lines)
    stack_2 = deepcopy(stack_1)
    print("Solution day1 : {}".format(q1(file, glob_lines, stack_1)))
    print("Solution day2 : {}".format(q2(file, glob_lines, stack_2)))
