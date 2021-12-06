import functools as func
import operator as op
from dataclasses import dataclass

from sol1 import Submarine, parse_input
from utils import allinput, compose, tupled


@dataclass
class SubmarineWithAim(Submarine):
    aim: int    

    def forward(self, dx):
        super().forward(dx)
        self.depth += self.aim * dx

    def submerge(self, x):
        self.aim += x


def main():
    text = allinput()

    submarine = SubmarineWithAim(0, 0, 0)

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
