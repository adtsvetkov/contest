import pytest

from .task import task3


class Case:
    def __init__(self, name: str, n: int, m: int, pixels: list, optimal_cost: int):
        self._name = name
        self.n = n
        self.m = m
        self.pixels = pixels
        self.optimal_cost = optimal_cost

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n = 7,
        m = 9,
        pixels=[(1, 1), 
                (7, 8), 
                (3, 2), 
                (5, 3), 
                (2, 8), 
                (4, 8), 
                (3, 6)],
        optimal_cost = 2,
    ),
    Case(
        name='base2',
        n = 5,
        m = 10,
        pixels=[(1, 1),
               (3, 2), 
               (5, 8), 
               (3, 6),
               (1, 8)],
        optimal_cost = 3,
    ),
     Case(
        name='base3',
        n = 9,
        m = 10,
        pixels=[(1, 1),
               (6, 6), 
               (8, 4)],
        optimal_cost = -1,
    ),
    Case(
        name='base4',
        n = 4,
        m = 4,
        pixels=[(1, 1), (2, 1), (2, 3), (3, 3), (4, 3)],
        optimal_cost = 2,
    ),
    Case(
        name='base5',
        n = 5,
        m = 5,
        pixels=[(1, 1), (2, 1), (3, 1), (3, 2)],
        optimal_cost = -1,
    ),
    Case(
        name='base6',
        n = 2,
        m = 2,
        pixels=[(1, 1), (1, 2), (2, 1), (2, 2)],
        optimal_cost = 0,
    ),
    Case(
        name='base7',
        n = 5,
        m = 5,
        pixels=[(1, 1), (2, 2), (3, 3), (4, 4)],
        optimal_cost = 3,
    ),
    Case(
        name='base8',
        n = 6,
        m = 7,
        pixels=[(1, 1), (6, 1)],
        optimal_cost = 2,
    ),
    Case(
        name='base9',
        n = 6,
        m = 7,
        pixels=[(1, 1), (3, 2)],
        optimal_cost = -1,
    ),
    Case(
        name='base10',
        n = 3,
        m = 4,
        pixels=[(1, 1), (2, 1)],
        optimal_cost = 1,
    ),
    Case(
        name='base11',
        n = 5,
        m = 6,
        pixels=[(1, 1), (2, 1), (3, 1), (4, 1)],
        optimal_cost = 1,
    ),
    Case(
        name='base12',
        n = 5,
        m = 6,
        pixels=[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
        optimal_cost = 1,
    ),
    Case(
        name='base13',
        n = 3,
        m = 3,
        pixels=[(1, 1), (3, 3)],
        optimal_cost = 1,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    cost = task3(n = case.n, m = case.m, pixels=case.pixels)
    assert cost == case.optimal_cost
