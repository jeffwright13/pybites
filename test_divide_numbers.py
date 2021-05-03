from divide_numbers import divide_numbers
import pytest



def test_divide_numbers_div_zero():
    # Define the function that will cause the exception
    def divide_by_zero():
        divide_numbers(1, 0)
    # This syntax will check that the expected Exception is raised
    with pytest.raises(ZeroDivisionError):
        divide_by_zero()

def test_divide_numbers_div_zero_alternate_method():
    # This is an alternate syntax that does the same thing:
    # pytest.raises(ExpectedException, func, *args, **kwargs)
    def divide_by_zero(tup):
        divide_numbers(tup[0], tup[1])
    pytest.raises(ZeroDivisionError, divide_by_zero, (1, 0))

@pytest.mark.parametrize(
    "numerator, denominator, expected",
    [
        (1, 1, 1),
        (2, 2, 1),
        (3, 3, 1),
        (-1, -1, 1),
        (-2, -2, 1),
        (1, 2, 0.5),
    ],
)
def test_divide_numbers(numerator, denominator, expected):
    assert divide_numbers(numerator, denominator) == expected
