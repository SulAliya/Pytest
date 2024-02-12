from utils import arrs
import pytest



@pytest.fixture
def coll():
    return [1, 2, 3]


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice(coll, None) == [1, 2, 3]


