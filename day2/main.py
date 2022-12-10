from helper.helper import FileHelper


Enemy = {'A': 1, 'B': 2, 'C': 3}
Myself = {'X': 1, 'Y': 2, 'Z': 3}
# First beat second
Winner = {'A': 'Z', 'B': 'X', 'C': 'Y'}
# Second beat first
Loser = {'A': 'Y', 'B': 'Z', 'C': 'X'}


def q2(lines):
    total = 0
    for line in lines:
        if line[2] == 'X':
            total += Myself[Winner[line[0]]]
            total += 0
        elif line[2] == 'Y':
            total += Enemy[line[0]]
            total += 3
        elif line[2] == 'Z':
            total += Myself[Loser[line[0]]]
            total += 6

    return total


def q1(lines):
    total = 0
    for line in lines:
        if Loser[line[0]] == line[2]:
            total += 6
        elif Winner[line[0]] == line[2]:
            total += 0
        else:
            total += 3
        total += Myself[line[2]]

    return total

if __name__ == "__main__":
    file = FileHelper("day2//input.txt")
    glob_lines = file.get_lines()
    print("Solution day1 : {}".format(q1(glob_lines)))
    print("Solution day2 : {}".format(q2(glob_lines)))
