import pytest
import bite037

expected_10 = """10
9
8
7
6
5
4
3
2
1
time is up
"""

expected_3 = """3
2
1
time is up
"""

expected_1 = """1
time is up
"""

expected_0 = """time is up
"""


def test_countdown_for_defaut_input(capfd):
    bite037.countdown_for()
    captured = capfd.readouterr()
    assert captured.err == ""
    assert captured.out == expected_10


@pytest.mark.parametrize(
    "input, expected",
    [
        (3, expected_3),
        (1, expected_1),
        (0, expected_0),
    ],
)
def test_countdown_for_nondefault(capfd, input, expected):
    bite037.countdown_for(input)
    captured = capfd.readouterr()
    assert captured.err == ""
    assert captured.out == expected


def test_countdown_recursion_defaut_input(capfd):
    bite037.countdown_recursive()
    captured = capfd.readouterr()
    assert captured.err == ""
    assert captured.out == expected_10


@pytest.mark.parametrize(
    "input, expected",
    [
        (3, expected_3),
        (1, expected_1),
        (0, expected_0),
    ],
)
def test_countdown_recursion_nondefault(capfd, input, expected):
    bite037.countdown_recursive(input)
    captured = capfd.readouterr()
    assert captured.err == ""
    assert captured.out == expected
