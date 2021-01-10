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
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    count = task1(transitions=case.transitions, mouses = case.mouses)
    assert count == case.optimal_count

