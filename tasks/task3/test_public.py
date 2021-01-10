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
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    cost = task3(n = case.n, m = case.m, pixels=case.pixels)
    assert cost == case.optimal_cost
