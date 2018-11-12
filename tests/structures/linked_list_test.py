import pytest
from structures.linked_list import LinkedList

_test_data = [
    range(1, 11),
    [0, 6, 7, 12, 9, 10]
]

@pytest.mark.parametrize('data', _test_data)
def test_list(data):
    ll = LinkedList(data=data)
    assert len(ll) == len(data)
    for e in ll:
        assert e in data
    for e in data:
        assert e in ll