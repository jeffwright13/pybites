from datetime import datetime, timedelta
import pytest
from bite019 import Promo


def test_basic_constructor():
    P = Promo("testname", datetime.now())
    assert "_name" in P.__dict__
    assert "_expires" in P.__dict__


def test_constructor_wrong_types():
    def give_int_instead_of_string():
        Promo(5, datetime.now())

    def give_str_instead_of_datetime():
        Promo("some_string", "bad_datetime")

    with pytest.raises(AssertionError):
        give_int_instead_of_string()

    with pytest.raises(AssertionError):
        give_str_instead_of_datetime()


def test_not_expired():
    P1 = Promo("P1", datetime.now() + timedelta(seconds=10))
    assert P1.expired == False


def test_expired():
    P1 = Promo("P1", datetime.now() + timedelta(seconds=-1))
    assert P1.expired == True
