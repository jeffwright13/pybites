import pytest
from bite029 import get_index_different_char


@pytest.mark.parametrize(
    "chars, expected",
    [
        (["A", "f", ".", "Q", 2], 2),
        ([".", "{", " ^", "%", "a"], 4),
        ([1, "=", 3, 4, 5, "A", "b", "a", "b", "c"], 1),
        (["", "", "e"], 2),
        (["", "", 1], 2),
        # (["", "", 15], 2),
        (["=", "=", "", "/", "/", 9, ":", ";", "?"], 5),
        (["=", "=", "", "/", "/", 9, ":", ";", "?", "¡"], 5),
    ],
)
def test_get_index_different_char(chars, expected):
    assert get_index_different_char(chars) == expected


def test_get_index_different_char_bad_input():
    def give_bad_input():
        get_index_different_char([])
        get_index_different_char([3, "."])
        get_index_different_char([3, "f", ".", "Q", ":"])
        get_index_different_char(["'", ",", ".", "Q", "Q"])
        get_index_different_char(["f", "f", ".", "Q", ":"])

    with pytest.raises(ValueError):
        give_bad_input()
