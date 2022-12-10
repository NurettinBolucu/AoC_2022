from helper.helper import FileHelper


Enemy = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
         'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
         's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


def q2(lines):
    total = 0
    ctr = 0
    for line in lines:
        if ctr == 0:
            a_s = set(line[0:len(line)-1])
            ctr += 1
        elif ctr == 1:
            b_s = set(line[0:len(line)-1])
            ctr += 1
        else:
            c_s = set(line[0:len(line)-1])
            ctr = 0
            
            if 'a_s' not in locals() or 'b_s' not in locals():
                raise RuntimeError("Problem occurred")
            found = a_s & b_s & c_s

            (element,) = found
            if found is None:
                raise RuntimeError("Failed for {}".format(line))

            if 'A' <= element <= 'Z':
                total += Enemy[element.lower()]
                total += 26
            else:
                total += Enemy[element]

    return total


def q1(lines):
    total = 0
    for line in lines:
        _len = len(line)
        a_s = set(line[0:int((_len-1)/2)])
        b_s = set(line[int((_len-1)/2):_len-1])
        found = a_s & b_s
        (element,) = found
        if found is None:
            raise RuntimeError("Failed for {}".format(line))

        if 'A' <= element <= 'Z':
            total += Enemy[element.lower()]
            total += 26
        else:
            total += Enemy[element]
    return total


if __name__ == "__main__":
    file = FileHelper("day3//input.txt")
    glob_lines = file.get_lines()
    print("Solution day1 : {}".format(q1(glob_lines)))
    print("Solution day2 : {}".format(q2(glob_lines)))
