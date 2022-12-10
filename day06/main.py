from helper.helper import FileHelper


def q1(lines):
    st = []
    ln = len(lines[0])
    line = lines[0]
    for i in range(ln):
        if i < 4:
            st.append(line[i])
        else:
            st.pop(0)
            st.append(line[i])
            at = set(st)
            if len(at) == 4:
                return i+1


def q2(lines):
    st = []
    ln = len(lines[0])
    line = lines[0]
    for i in range(ln):
        if i < 14:
            st.append(line[i])
        else:
            st.pop(0)
            st.append(line[i])
            at = set(st)
            if len(at) == 14:
                return i+1


if __name__ == "__main__":
    file = FileHelper("day06//input.txt")
    glob_lines = file.get_lines()
    print("Solution 1 : {}".format(q1(glob_lines)))
    print("Solution 2 : {}".format(q2(glob_lines)))
