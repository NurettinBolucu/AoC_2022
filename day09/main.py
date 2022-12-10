from helper.helper import FileHelper
from enum import Enum


class Direction(Enum):
    Up = [1, 0]
    Down = [-1, 0]
    Right = [0, 1]
    Left = [0, -1]


Directions = {'U': Direction.Up, 'D': Direction.Down,
              'R': Direction.Right, 'L': Direction.Left}


def q1(lines):
    arr = []
    x = 750
    y = 750
    for i in range(x*2):
        arr.append([0]*(x*2))
    head = []
    tail = [x, y]
    tails = []
    for i in range(9):
        tails.append([750, 750])
    for line in lines:
        _direction = Directions[line[0]]
        for s in range(int(line[1])):
            x += _direction.value[0]
            y += _direction.value[1]
            prev_head = head[:]
            head = [x, y]
            diff = abs(head[0]-tail[0]) + abs(head[1]-tail[1])
            if diff > 2:
                tail = prev_head[:]
            elif diff == 2:
                if head[0] == tail[0] or head[1] == tail[1]:
                    tail = prev_head[:]
            arr[tail[0]][tail[1]] = 1

    total = 0
    for i in range(len(arr)):
        total += sum(arr[i])
    return total


def q2(lines):
    x = 2000
    y = 2000
    arr = []
    for i in range(x*2):
        arr.append([0]*(y*2))
    tails = []
    for i in range(9):
        tails.append([x, y])
    for line in lines:
        _direction = Directions[line[0]]
        for s in range(int(line[1])):
            x += _direction.value[0]
            y += _direction.value[1]
            head = [x, y]
            prev = head[:]
            for i in range(9):
                diff = abs(prev[0]-tails[i][0]) + abs(prev[1]-tails[i][1])
                if diff > 2:
                    tails[i][0] += +1 if (prev[0]-tails[i][0]) > 0 else -1
                    tails[i][1] += +1 if (prev[1]-tails[i][1]) > 0 else -1
                elif diff == 2:
                    if prev[0] == tails[i][0] or prev[1] == tails[i][1]:
                        tails[i][0] += +1 if (prev[0]-tails[i][0]) > 0 else (0 if (prev[0]-tails[i][0]) == 0 else -1)
                        tails[i][1] += +1 if (prev[1]-tails[i][1]) > 0 else (0 if (prev[1]-tails[i][1]) == 0 else -1)
                prev = tails[i][:]

            arr[tails[8][0]][tails[8][1]] = 1
    total = 0
    for i in range(len(arr)):
        total += sum(arr[i])
    return total


if __name__ == "__main__":
    file = FileHelper("day09//input.txt")
    glob_lines = file.get_seperated_lines(' ')

    print("Solution 1: " + str(q1(glob_lines)))
    print("Solution 2: " + str(q2(glob_lines)))
