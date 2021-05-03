import pytest
from bite001 import sum_numbers


def test_sum_numbers_none():
    assert sum_numbers() == 5050


def test_sum_numbers_strings():
    def pass_strings_as_params():
        sum_numbers("a", "b")

    with pytest.raises(TypeError):
        pass_strings_as_params()


@pytest.mark.parametrize(
    "input_list, expected_sum",
    [
        ([1, 0, -1], 0),
        ([-100, -10, 0, 6,], -104),
        ([-1.0, 0, 0, 6.5,], 5.5),
        ([-10.0, 0, 0, 4,], -6.0),
    ],
)
def test_sum_numbers(input_list, expected_sum):
    assert sum_numbers(input_list) == expected_sum
