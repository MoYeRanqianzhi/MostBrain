from interpreter import *
from termcolor import colored
from colorama import initialise

import sys

initialise.init()


def print_err(value):
    sys.stdout.write(
        colored(
            text=value + '\n',
            color='light_red'
        )
    )


def err(type, value, traceback):
    print_err('这有一个报错，但是具体是什么错误呢~这是一个秘密♥就不告诉你~就不告诉你~')


sys.excepthook = err


def decode(code, mb):
    return [
        {
            '>': mb.move,
            '<': mb.change,
            '+': mb.add,
            '.': mb.output,
            ':': mb.cmd,
            ',': mb.input,
            '[': mb.goon,
            ']': mb.goto
        }[c]
        for c in code
        if c in ('>', '<', '+', '.', ':', ',', '[', ']')
    ]


def main(mb: MostBrain):
    if len(sys.argv) >= 2:
        if os.path.exists(sys.argv[1]):
            with open(sys.argv[1], mode='r', encoding='utf-8') as f:
                code = f.read()
            mb.execute(decode(code, mb))
        else:
            print_err('你所运行的文件不存在！说！你是不是在耍我！')
    else:
        code = ''
        while not code.lower() == 'exit':
            code = input('>_< ')
            mb.execute(decode(code, mb))


if __name__ == '__main__':
    main(MostBrain())
