from helper.helper import FileHelper


def solution(glob_lines):
    lines = []
    rows = len(glob_lines)
    columns = len(glob_lines[0]) - 1
    for i in range(rows):
        lines.append([])
        for s in range(columns):
            if glob_lines[i][s] == 'S':
                lines[i].append(ord('z') - ord('a') + 2)
                _end = [i, s]
            elif glob_lines[i][s] == 'E':
                lines[i].append(0)
                _start = [i, s]
            else:
                lines[i].append(ord('z') - ord(glob_lines[i][s]) + 1)

    visited = [[0]*columns for i in range(rows)]
    visited[_start[0]][_start[1]] = 1

    queue = [_start]
    values_in_queue = [lines[_start[0]][_start[1]]]
    total = 0
    closest_to_a = 0
    closest_to_S = 0
    while len(queue) > 0:
        total += 1
        for i in range(len(queue)):
            node = queue[0]
            queue.pop(0)
            values_in_queue.pop(0)
            if (node[1]+1 < columns) and (lines[node[0]][node[1]]+1 >= lines[node[0]][node[1]+1]) and visited[node[0]][node[1] + 1] == 0:
                visited[node[0]][node[1] + 1] = 1
                queue.append([node[0], node[1]+1])
                values_in_queue.append(lines[node[0]][node[1]+1])
            if (node[0]+1 < rows) and (lines[node[0]][node[1]]+1 >= lines[node[0]+1][node[1]]) and visited[node[0] + 1][node[1]] == 0:
                visited[node[0]+1][node[1]] = 1
                queue.append([node[0]+1, node[1]])
                values_in_queue.append(lines[node[0]+1][node[1]])
            if (node[0]-1 >= 0) and (lines[node[0]][node[1]]+1 >= lines[node[0]-1][node[1]]) and visited[node[0] - 1][node[1]] == 0:
                visited[node[0]-1][node[1]] = 1
                queue.append([node[0]-1, node[1]])
                values_in_queue.append(lines[node[0]-1][node[1]])
            if (node[1]-1 >= 0) and (lines[node[0]][node[1]]+1 >= lines[node[0]][node[1]-1]) and visited[node[0]][node[1] - 1] == 0:
                visited[node[0]][node[1] - 1] = 1
                queue.append([node[0], node[1]-1])
                values_in_queue.append(lines[node[0]][node[1]-1])
        if ((ord('z') - ord('a') + 1) in values_in_queue) and closest_to_a == 0:
            closest_to_a = total
        if (_end in queue) and closest_to_S == 0:
            closest_to_S = total

        if closest_to_S != 0 and closest_to_a != 0:
            return [closest_to_S, closest_to_a]


if __name__ == "__main__":
    file = FileHelper("day12//input.txt")
    glob_lines = file.get_lines()

    solutions = solution(glob_lines)
    if solutions is None:
        print("Something missing")
    else:
        print("Solution 1: {}".format(solutions[0]))
        print("Solution 2: {}".format(solutions[1]))
