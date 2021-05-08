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


def test_rotate_zero():
    assert bite008.rotate("Fred0", 0) == "Fred0"


def test_rotate_n_positive_equal_or_greater():
    assert bite008.rotate("Fred0", 5) == "Fred0"
    assert bite008.rotate("Fred0", 6) == "Fred0"


def test_rotate_n_positive_less_than():
    assert bite008.rotate("Fred0", 4) == "0Fred"
    assert bite008.rotate("Fred0", 3) == "d0Fre"


def test_rotate_n_negative_equal_or_greater():
    assert bite008.rotate("Fred0", -5) == "Fred0"
    assert bite008.rotate("Fred0", -6) == "Fred0"


def test_rotate_n_negative_less_than():
    assert bite008.rotate("Fred0", -4) == "red0F"
    assert bite008.rotate("Fred0", -3) == "ed0Fr"
