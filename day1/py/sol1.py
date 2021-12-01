import functools as func
import operator as op

from utils import allinput, compose


def diff(xs):
    def _(acc, x):
        if acc:
            ys, last = acc
            return [*ys, x - last], x
        return [], x

    return func.reduce(_, xs, None)[0]


def count_increases(xs):
    return compose(
        sum,
        func.partial(map, func.partial(op.lt, 0)),
        diff,
    )(xs)


def main():
    text = allinput()

    compose(
        print,
        count_increases,
        func.partial(map, int),
        op.methodcaller('split', sep='\n'),
    )(text)


example = """199
200
208
210
200
207
240
269
260
263"""


if __name__ == '__main__':
    main()
