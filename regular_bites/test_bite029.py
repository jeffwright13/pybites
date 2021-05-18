import pytest
from bite029 import get_index_different_char


@pytest.mark.parametrize(
    "chars, expected",
    [
        (["A", "f", ".", "Q", 2], 2),
        ([".", "{", " ^", "%", "a"], 4),
        ([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],1)
    ],
)
def test_get_index_different_char(chars, expected):
    assert get_index_different_char(chars) == expected
