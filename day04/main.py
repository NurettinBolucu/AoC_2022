from helper.helper import FileHelper


def q2(lines):
    total = 0
    seps = [',', '-']
    default_sep = seps[0]

    for line in lines:
        for sep in seps[1:]:
            line = line.replace(sep, default_sep)
        line = [i.strip() for i in line.split(default_sep)]
        a1 = [int(line[0]), int(line[1])]
        a2 = [int(line[2]), int(line[3])]
        if a1[0] < a2[0]:
            if a2[0] <= a1[1]:
                total += 1
        else:
            if a1[0] <= a2[1]:
                total += 1

    return total


def q1(lines):
    total = 0
    seps = [',', '-']
    default_sep = seps[0]

    for line in lines:
        for sep in seps[1:]:
            line = line.replace(sep, default_sep)
        line = [i.strip() for i in line.split(default_sep)]
        a1 = [int(line[0]), int(line[1])]
        a2 = [int(line[2]), int(line[3])]
        if (a1[1] - a1[0]) > (a2[1] - a2[0]):
            bigger = a1
            lower = a2
        else:
            bigger = a2
            lower = a1

        if bigger[0] <= lower[0] and bigger[1] >= lower[1]:
            total += 1
    return total



if __name__ == "__main__":
    file = FileHelper("day04//input.txt")
    glob_lines = file.get_lines()
    print("Solution 1 : {}".format(q1(glob_lines)))
    print("Solution 2 : {}".format(q2(glob_lines)))
