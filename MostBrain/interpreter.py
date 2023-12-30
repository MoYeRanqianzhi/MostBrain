import sys
import os


class Box:
    def __init__(self):
        self.data = {}

    def __getitem__(self, item):
        if isinstance(item, int):
            if self.data.get(item) is not None:
                return self.data.get(item)
            else:
                return 0

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.data.update(
                {
                    key: value
                }
            )


class Pointer:
    def __init__(self, box: Box):
        self.index = 0
        self.box = box

    @property
    def value(self):
        return self.box[self.index]

    @value.setter
    def value(self, value):
        self.box[self.index] = value

    def __add__(self, other):
        self.box[self.index] += other
        return self.index

    def __gt__(self, other):
        self.index += other
        return self.index


class MostBrain:
    def __init__(self):
        self.box = Box()
        self.pointer = Pointer(self.box)
        self.unit = 1
        self.temp = ''
        self.skip = False
        self.loop = []

        self.index = 0

    def move(self):
        return self.pointer > self.unit

    def add(self):
        return self.pointer + self.unit

    def change(self):
        self.unit = - self.unit
        return self.unit

    def output(self):
        sys.stdout.write(chr(self.pointer.value))
        sys.stdout.flush()

    def cmd(self):
        if chr(self.pointer.value) == '\n':
            os.system(self.temp)
            self.temp = ''
        else:
            self.temp += chr(self.pointer.value)

    def input(self):
        self.pointer.value = ord(sys.stdin.read(1))

    def goon(self):
        self.loop.append(self.index)
        if not self.pointer.value:
            self.skip = True

    def goto(self):
        if self.skip:
            self.skip = False
        else:
            if self.pointer.value:
                self.index = self.loop[-1]

    def execute(self, command):
        self.index = 0
        while self.index <= len(command) - 1:
            if not self.skip:
                command[self.index]()
            self.index += 1


# if __name__ == '__main__':
#     m = MostBrain()
#     code = "+" * 99 + ":>" + "+" * 109 + ":>" + "+" * 100 + ':>' + "+" * 10 + ":"
#
#     # method = {
#     #     'move': m.move,
#     #     'change': m.change,
#     #     'add': m.add,
#     #     'output': m.output,
#     #     'input': m.input,
#     #     'goon': m.goon,
#     #     'goto': m.goto,
#     # }
#     method = {
#         '>': m.move,
#         '<': m.change,
#         '+': m.add,
#         '.': m.output,
#         ':': m.cmd,
#         ',': m.input,
#         '[': m.goon,
#         ']': m.goto,
#     }
#
#     # c = {
#     #     '>': 'move',
#     #     '<': 'change',
#     #     '+': 'add',
#     #     '.': 'output',
#     #     ',': 'input',
#     #     '[': 'goon',
#     #     ']': 'goto',
#     # }
#
#     # print(';\n'.join([c[i] for i in code]))
#     # m.execute([method[i] for i in code.replace('\n', '').replace(' ', '').split(';') if i])
#     m.execute([method[i] for i in code])
#
