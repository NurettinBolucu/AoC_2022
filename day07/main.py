from helper.helper import FileHelper


class Directory:
    def __init__(self, name):
        self.name = name
        self.directories = []
        self.files = []
        self.size = 0

    def get_dir_by_name(self, nm):
        for i in range(len(self.directories)):
            if nm == self.directories[i].name:
                return self.directories[i]


def find_directories(fl, root, lines, i):
    global total

    while True:
        try:
            ln = fl.split_line(lines[i], " ")
        except:
            return root.size, i

        if ln[0] == "dir":
            root.directories.append(Directory(ln[1]))
        elif ln[0] == '$':
            if ln[1] == "cd" and ln[2] == "..":
                return root.size, i
            elif ln[1] == "cd":
                dir = root.get_dir_by_name(ln[2])
                sz, i = find_directories(fl, dir, lines, i+1)
                root.size += sz
        else:
            root.size += int(ln[0])
        i += 1


total = 0


def q1(root):
    global total
    if root.size < 100000:
        total += root.size
    for dir in root.directories:
        q1(dir)


minimum_size = 0
minimum_found = 0


def q2(root):
    global minimum_found
    if minimum_size < root.size < minimum_found:
        minimum_found = root.size
    for dir in root.directories:
        q2(dir)


if __name__ == "__main__":
    file = FileHelper("day07//input.txt")
    glob_lines = file.get_lines()
    root_gl = Directory('/')
    glob_total = 0
    s, _ = find_directories(file, root_gl, glob_lines, 1)
    q1(root_gl)
    print("Solution 1: " + str(total))
    minimum_size = s - 40000000
    mimumum_found = s
    q2(root_gl)
    print("Solution 2: " + str(mimumum_found))
