import fileinput
import functools as func
import sys


def compose(*F):
    return func.reduce(lambda f, g: lambda x: f(g(x)), F)


def allinput():
    lines = []
    for line in fileinput.input():
        lines.append(line)
    return ''.join(lines)


def tupled(fn):
    def fn_(x):
        return fn(*x)
    return fn_


def tuple_map(*fs):
    return compose(
        tuple,
        func.partial(map, tupled(lambda i, v: fs[i](v) if i < len(fs) and fs[i] else v)),
        enumerate,
    )


def identity(x):
    return x


def log(x):
    print(x, file=sys.stderr)
    return x
