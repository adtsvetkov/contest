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
    Case(
        name='base3',
        coords=[(1, 7), (6, 7)],
        city=[(4, 2), (4, 12), (3, 12), (3, 2)],
        optimal_cost = 6.000000,
    ),
    Case(
        name='base4',
        coords=[(-1, 0), (2, 0)],
        city=[(0, 0), (1, 0), (1, 1), (0, 1)],
        optimal_cost = 3.000000,
    ),
    Case(
        name='base5',
        coords=[(-70, -86), (31, -90)],
        city=[(-92, -70), (77, -51), (99, 23), (72, 52), (-34, 86)],
        optimal_cost = 101.079177,
    ),
    Case(
        name='base6',
        coords=[(88, 37), (71, -14)],
        city=[(48, -22), (61, -47), (48, 72), (-81, 92)],
        optimal_cost = 53.758720,
    ),
    Case(
        name='base7',
        coords=[(84, -49), (75, -39)],
        city=[(-87, -67), (-12, -58), (97, 79)],
        optimal_cost = 13.453624,
    ),
    Case(
        name='base8',
        coords=[(0, 0), (90, 0)],
        city=[(10, 0), (20, -90), (20, 90)],
        optimal_cost = 100.000000,
    ),
    Case(
        name='base9',
        coords=[(90, 85), (-90, 85)],
        city=[(0, 0), (1, 100), (-1, 100)],
        optimal_cost = 181.700000,
    ),
    Case(
        name='base10',
        coords=[(-100, 0), (100, 0)],
        city=[(-99, -100), (99, -100), (99, 100), (-99, 100)],
        optimal_cost = 398.000000,
    ),
    Case(
        name='base11',
        coords=[(-100, -100), (100, 100)],
        city=[(1, 1), (5, 1), (5, 5), (1, 5)],
        optimal_cost = 285.185858,
    ),
    Case(
        name='base12',
        coords=[(94, -63), (93, -24)],
        city=[(-94, -89), 
              (-91, -95), 
              (-4, -100), 
              (81, -98), 
              (93, -80), 
              (92, 17), 
              (82, 90), 
              (-43, 100), 
              (-86, 93), 
              (-97, -10)],
        optimal_cost = 39.012818,
    ),
    Case(
        name='base13',
        coords=[(0, 0), (3, 3)],
        city=[(1, 1), (4, 1), (4, 2), (0, 2)],
        optimal_cost = 5.656854,
    ),
    Case(
        name='base14',
        coords=[(2, 2), (-2, -2)],
        city=[(-1, -1), (1, -1), (1, 1), (-1, 1)],
        optimal_cost = 6.828427,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    cost = task2(coords=case.coords, city = case.city)
    assert cost == case.optimal_cost
