"""
Bite 19. Write a property

Write a simple Promo class. Its constructor receives two variables: name (which must be a string) and expires (which must be a datetime object).

Add a property (https://docs.python.org/3/library/functions.html#property) called expired which returns a boolean value indicating whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!
"""
from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        assert isinstance(name, str)
        assert isinstance(expires, datetime)
        self._name = name
        self._expires = expires

    @property
    def expired(self):
        return self._expires < datetime.now()
