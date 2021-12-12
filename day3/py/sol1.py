import collections as colls
import functools as func
import operator as op

from utils import allinput, compose, fst, identity, log, tuple_map, tupled


def parse_input(text):
    return compose(
        func.partial(map, list),
        op.methodcaller('split', '\n'),
    )(text)


def transpose(rows):
    columns = []

    for i, row in enumerate(rows):
        for j, x in enumerate(row):
            columns[j][i] = x

    return columns


def main():
    # text = example
    text = allinput()

    report = compose(
        list,
        parse_input,
    )(text)

    column_occurrences = get_column_occurrences(report)

    gamma_rate = get_gamma_rate(column_occurrences)
    epsilon_rate = get_epsilon_rate(column_occurrences)

    print(gamma_rate * epsilon_rate)


def get_column_occurrences(report):
    counters = [colls.Counter() for _ in range(len(report[0]))]

    for row in report:
        for j, x in enumerate(row):
            counters[j][x] += 1

    return counters


def get_gamma_rate(counters: list[colls.Counter]):
    return compose(
        func.partial(int, base=2),
        ''.join,
        func.partial(map, compose(
            fst,
            fst,
            op.methodcaller('most_common', 1),
        )),
    )(counters)


def get_epsilon_rate(counters):
    return compose(
        func.partial(int, base=2),
        ''.join,
        func.partial(map, compose(
            fst,
            op.itemgetter(-1),
            op.methodcaller('most_common'),
        )),
    )(counters)


example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

# answer to example 198


if __name__ == '__main__':
    main()
