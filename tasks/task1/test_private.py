import pytest

from .task import task1


class Case:
    def __init__(self, name: str, transitions: list, mouses: list, optimal_count: int):
        self._name = name
        self.transitions = transitions
        self.mouses = mouses
        self.optimal_count = optimal_count

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        transitions=[1, 1],
        mouses=[2, 0, 0],
        optimal_count = 1,
    ),
    Case(
        name='base2',
        transitions=[1],
        mouses=[3, 0],
        optimal_count = 3,
    ),
    Case(
        name='base3',
        transitions=[1, 1],
        mouses=[3, 1, 2],
        optimal_count = 3,
    ),
    Case(
        name='base4',
        transitions=[1, 1],
        mouses=[3, 1, 3],
        optimal_count = 4,
    ),
    Case(
        name='base5',
        transitions=[1, 1, 1, 4],
        mouses=[28, 0, 0, 0, 0],
        optimal_count = 10,
    ),
    Case(
        name='base6',
        transitions=[1],
        mouses=[91, 0],
        optimal_count = 91,
    ),
    Case(
        name='base7',
        transitions=[1, 1, 2, 4, 4, 3, 6, 1, 5],
        mouses=[44, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        optimal_count = 11,
    ),
    Case(
        name='base8',
        transitions=[1, 2, 3, 4, 5, 6, 7, 8, 9],
        mouses=[92, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        optimal_count = 92,
    ),
    Case(
        name='base9',
        transitions=[1],
        mouses=[74, 73],
        optimal_count = 147,
    ),
    Case(
        name='base10',
        transitions=[1, 1, 1, 1, 1, 1, 1, 1, 1],
        mouses=[77, 10, 36, 51, 50, 82, 8, 56, 7, 26],
        optimal_count = 82,
    ),
    Case(
        name='base11',
        transitions=[1, 1],
        mouses=[0, 0, 0],
        optimal_count = 0,
    ),
    Case(
        name='base12',
        transitions=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
        mouses=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        optimal_count = 2,
    ),
    Case(
        name='base13',
        transitions=[1, 1, 2, 2, 3, 3, 4, 4, 5],
        mouses=[0, 0, 1000, 0, 0, 0, 0, 0, 0, 0],
        optimal_count = 500,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    count = task1(transitions=case.transitions, mouses = case.mouses)
    assert count == case.optimal_count
