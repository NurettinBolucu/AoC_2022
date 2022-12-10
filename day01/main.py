from helper.helper import FileHelper

if __name__ == "__main__":
    file = FileHelper("day01//input_1.txt")
    lines = file.get_lines()
    values = [0, 0, 0]
    most = 0
    total = 0
    for line in lines:
        if line == '\n':
            if total > min(values):
                values[0] = total
                values.sort()
            total = 0
        else:
            total += int(line)

    print("Solution 1 : {}".format(values[0]))
    print("Solution 2 : {}".format(values[0]+values[1]+values[2]))
