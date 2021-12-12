import collections as colls
import functools as func
import operator as op

from sol1 import parse_input
from utils import allinput, compose


def main():
    # text = example
    text = allinput()

    report = compose(
        list,
        parse_input,
    )(text)

    oxygen_generator_rating = get_oxygen_generator_rating(report)

    CO2_scrubber_rating = get_CO2_scrubber_rating(report)

    print(oxygen_generator_rating * CO2_scrubber_rating)


def get_oxygen_generator_rating(report):
    i = 0

    while len(report) > 1:
        column_occurrences = get_column_occurrences(report, {i})

        [(most_occurred, a_occurrence), (_less_ocurred, b_occurrence)] = column_occurrences[i].most_common(2)

        a = most_occurred
        if a_occurrence == b_occurrence:
            a = '1'

        report = [
            y for y in report if y[i] == a
        ]

        i += 1

    return bitlist_to_int(report[0])


def get_CO2_scrubber_rating(report):
    i = 0

    while len(report) > 1:
        column_occurrences = get_column_occurrences(report, {i})

        [(_most_occurred, a_occurrence), (less_ocurred, b_occurrence)] = column_occurrences[i].most_common(2)

        a = less_ocurred
        if a_occurrence == b_occurrence:
            a = '0'

        report = [
            y for y in report if y[i] == a
        ]

        i += 1

    return bitlist_to_int(report[0])


bitlist_to_int = compose(
    func.partial(int, base=2),
    ''.join,
)


def get_column_occurrences(report, column_set: set[int] =None):
    if column_set is None:
        column_set = set(range(report[0]))
    else:
        column_set = set(column_set)

    counters = {c: colls.Counter() for c in column_set}

    for row in report:
        for j, x in enumerate(row):
            if j not in column_set:
                continue
            counters[j][x] += 1

    return counters



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

# answer to example 230


if __name__ == '__main__':
    main()
