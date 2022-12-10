

class FileHelper:

    def __init__(self, filename):
        self.__file = open("../" + filename, 'r')
        self.__all_lines = self.__file.readlines()

    def get_file(self):
        return self.__file

    def get_lines(self):
        return  self.__all_lines

    def get_lines_int(self):
        return [int(line) for line in self.__all_lines]

    @staticmethod
    def split_line(line, seps):
        default_sep = seps[0]

        # we skip seps[0] because that's the default separator
        for sep in seps[1:]:
            txt = line.replace(sep, default_sep)
        return [i.strip() for i in line.split(default_sep)]

    def get_seperated_lines(self, seps):
        return [self.split_line(line, seps) for line in self.__all_lines]

