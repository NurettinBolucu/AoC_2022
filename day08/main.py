from helper.helper import FileHelper


def q1(lines, traverse):
    total = 0
    for i in range(1, len(lines)-1):
        for x in range(1, len(lines[i])-2):
            if lines[i][x] > max(traverse[x][0:i]):
                total += 1
            elif lines[i][x] > max(traverse[x][i+1:len(traverse[x])]):
                total += 1
            elif lines[i][x] > max(lines[i][0:x]):
                total += 1
            elif lines[i][x] > max(lines[i][x+1:len(lines[i])]):
                total += 1
    total += (len(lines[0])-1 + (len(lines)-2))*2
    return total


def q2(lines, traverse):
    total = 0
    for i in range(1, len(lines)-1):
        for x in range(1, len(lines[i])-2):
            temp = 1

            # TOP
            if lines[i][x] > max(traverse[x][0:i]):
                mult = i
            else:
                a = [s for s in range(len(traverse[x][0:i])-1,-1,-1) if traverse[x][0:i][s] >= lines[i][x]]
                mult = i - a[0]
            temp *= mult

            # BOTTOM
            if lines[i][x] > max(traverse[x][i+1:len(traverse[x])]):
                mult = len(traverse[i]) - i - 1
            else:
                a = [s for s in range(len(traverse[x][i:len(traverse[x])])) if traverse[x][i:len(traverse[x])][s] >= lines[i][x]]
                mult = a[0] + 1
            temp *= mult

            # LEFT
            if lines[i][x] > max(lines[i][0:x]):
                mult = x
            else:
                a = [s for s in range(len(lines[i][0:x])-1,-1,-1) if lines[i][0:x][s] >= lines[i][x]]
                mult = x - a[0]
            temp *= mult

            # RIGHT
            if lines[i][x] > max(lines[i][x+1:len(lines[i])]):
                mult = len(lines[i]) - x - 2
            else:
                a = [s for s in range(len(lines[i][x+1:len(lines[i])])) if lines[i][x+1:len(lines[i])][s] >= lines[i][x]]
                mult = a[0] + 1
            temp *= mult

            if temp > total:
                total = temp

    return total


if __name__ == "__main__":
    file = FileHelper("day08//input.txt")
    glob_lines = file.get_lines()
    trees = []
    trees_traverse = []
    for i in glob_lines:
        trees.append(i)
    for x in range(len(glob_lines[0])-1):
        arr = ""
        for i in glob_lines:
            arr += i[x]
        trees_traverse.append(arr)

    print("Solution 1: " + str(q1(glob_lines, trees_traverse)))
    print("Solution 2: " + str(q2(glob_lines, trees_traverse)))
