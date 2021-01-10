import pytest

from .task import task2


class Case:
    def __init__(self, name: str, coords: list, city: list, optimal_cost: float):
        self._name = name
        self.coords = coords
        self.city = city
        self.optimal_cost = optimal_cost

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        coords=[(0, 3), (10, 3)],
        city=[(1, 0), (9, 0), (5, 3)],
        optimal_cost = 10.000000,
    ),
    Case(
        name='base2',
        coords=[(-90, 50), (90, 50)],
        city=[(0, 0), (1, 100), (-1, 100)],
        optimal_cost = 181.000000,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    cost = task2(coords=case.coords, city = case.city)
    assert cost == case.optimal_cost

