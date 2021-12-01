import fileinput
import sys
from functools import reduce


def compose(*F):
    return reduce(lambda f, g: lambda x: f(g(x)), F)


def allinput():
    lines = []
    for line in fileinput.input():
        lines.append(line)
    return ''.join(lines)


def log(x):
    print(x, file=sys.stderr)
    return x
