from helper.helper import FileHelper


class Monkey:
    def __init__(self, lines, monkey_no):
        self.monkey_no = monkey_no
        self._lines = lines
        self._initial_items = [int(item) for item in lines[0][3:]]
        self.items = [int(item) for item in lines[0][3:]]
        self._ctr = 0
        pass

    def get_counter(self):
        return self._ctr

    def get_divider(self):
        return int(self._lines[2][4])

    def reset(self):
        self.items = self._initial_items[:]
        self._ctr = 0

    def inspect(self, worry_level):
        if self._lines[1][5] == '*':
            worry_level *= (worry_level if self._lines[1][6] == "old" else int(self._lines[1][6]))
        elif self._lines[1][5] == '+':
            worry_level += (worry_level if self._lines[1][6] == "old" else int(self._lines[1][6]))
        self._ctr += 1
        return worry_level

    def test(self, worry_level):
        if worry_level % int(self._lines[2][4]) == 0:
            return int(self._lines[3][6])
        else:
            return int(self._lines[4][6])

    def add_item(self, worry_level):
        self.items.append(worry_level)

    def execute(self, worry_level, worry=False, mod=None):
        worry_level = self.inspect(worry_level)
        if not worry:
            worry_level = int(worry_level / 3)
        if mod is not None:
            worry_level = worry_level % mod
        new_monkey = self.test(worry_level)
        return [new_monkey, worry_level]


def calculate_rounds(_monkeys, round_count, worry, mod):
    for _ in range(round_count):
        for monkey in _monkeys:
            for j in range(len(monkey.items)):
                item = monkey.items.pop(0)
                new_monkey, new_worry_level = monkey.execute(item, worry, mod)
                _monkeys[new_monkey].add_item(new_worry_level)

    counters = []
    for monkey in monkeys:
        counters.append(monkey.get_counter())

    counters.sort(reverse=True)
    return counters[0] * counters[1]


def q1(_monkeys):
    return calculate_rounds(_monkeys, 20, False, None)


def q2(_monkeys):
    dividers = set()
    for monkey in monkeys:
        dividers.add(monkey.get_divider())
    mod = 1
    for divider in dividers:
        mod *= divider
    return calculate_rounds(_monkeys, 10000, True, mod)


if __name__ == "__main__":
    file = FileHelper("day11//input.txt")
    glob_lines = file.get_seperated_lines([' ', '    ', ', ', ':', '  '])
    monkeys = []
    for i in range(len(glob_lines)):
        if glob_lines[i][0] == "Monkey":
            monkeys.append(Monkey(glob_lines[i+1:i+6], int(glob_lines[i][1])))

    print("Solution 1: " + str(q1(monkeys)))

    for mon in monkeys:
        mon.reset()
    print("Solution 2: " + str(q2(monkeys)))
