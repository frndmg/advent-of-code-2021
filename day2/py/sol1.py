import functools as func
import operator as op
from dataclasses import dataclass

from utils import allinput, compose, identity, log, tuple_map, tupled


@dataclass
class Submarine:
    x: int
    depth: int

    def forward(self, dx):
        self.x += dx

    def submerge(self, ddepth):
        self.depth += ddepth

    def up(self, up):
        self.submerge(-up)

    def down(self, up):
        self.submerge(up)

    def execute(self, command, value):
        getattr(self, command)(value)


def parse_input(text):
    return compose(
        func.partial(map, compose(
            tuple_map(identity, int),
            op.methodcaller('split', ' '),
        )),
        op.methodcaller('split', '\n'),
    )(text)


def main():
    text = allinput()

    submarine = Submarine(0, 0)

    compose(
        list,
        func.partial(map, tupled(submarine.execute)),
        parse_input,
    )(text)

    print(submarine.x * submarine.depth)


example = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


if __name__ == '__main__':
    main()
