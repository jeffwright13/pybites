import bite008
import pytest

"""
@pytest.mark.parametrize(
    "test_input, expected",
    [(test_input1, expected1), ..., (test_inputN, expectedN)]
)
def test_function(test_input, expected):
    assert function(test_input) == expected
"""


@pytest.mark.parametrize(
    "s, n, expected",
    [("3+5", 0, "3+5"), ("01010", 1, "10100"), ("Hello!", -3, "lo!Hel")],
)
def test_rotate_simple(s, n, expected):
    assert bite008.rotate(s, n) == expected
