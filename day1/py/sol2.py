import functools as func
import itertools as its
import operator as op

from sol1 import count_increases
from utils import allinput, compose


def window(xs, n):
    it = iter(xs)
    x = tuple(its.islice(it, n))

    if len(x) == n:
        yield x

    for other in it:
        x = *x[1:], other
        yield x


def sum_windows(xs, n):
    return compose(
        func.partial(map, sum),
        func.partial(window, n=n),
    )(xs)


def main():
    text = allinput()

    compose(
        print,
        count_increases,
        func.partial(sum_windows, n=3),
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
