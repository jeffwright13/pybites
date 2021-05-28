import pytest
import bite037

expected = \
"""10
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

def test_correct_output():
    assert bite037.countdown_for() == expected
