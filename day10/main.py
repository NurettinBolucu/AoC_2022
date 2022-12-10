from helper.helper import FileHelper


def q1(lines):
    total = 0
    X = 1
    ctr = 1
    for line in lines:
        if line[0] == 'noop':
            if ctr % 40 == 20:
                total += ctr * X
            ctr += 1
        else:
            for s in range(2):
                if ctr % 40 == 20:
                    total += ctr * X
                ctr += 1
            X += int(line[1])
    return total


def q2(lines):
    Cycle = ""
    X = 1
    ctr = 1
    for line in lines:
        if line[0] == 'noop':
            if X+3 > (ctr % 40) >= X:
                Cycle += '#'
            else:
                Cycle += '.'
            ctr += 1
        else:
            for s in range(2):
                if X+3 > (ctr % 40) >= X:
                    Cycle += '#'
                else:
                    Cycle += '.'
                ctr += 1
            X += int(line[1])
    for i in range(int(len(Cycle) / 40)):
        print(Cycle[i*40:(i+1)*40])


if __name__ == "__main__":
    file = FileHelper("day10//input.txt")
    glob_lines = file.get_seperated_lines(' ')

    print("Solution 1: " + str(q1(glob_lines)))
    print("Solution 2: ")
    q2(glob_lines)
