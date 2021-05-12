"""


    Write a generator that returns every 100th day counting forward from the PYBITES_BORN date.

    Here is how the generator would work if you import and use it in your REPL:

    >>> from itertools import islice
    >>> from pprint import pprint as pp
    >>> from gendates import gen_special_pybites_dates
    >>> gen = gen_special_pybites_dates()
    >>> pp(list(islice(gen, 5)))
    [datetime.datetime(2017, 3, 29, 0, 0),
     datetime.datetime(2017, 7, 7, 0, 0),
     datetime.datetime(2017, 10, 15, 0, 0),
     datetime.datetime(2018, 1, 23, 0, 0),
     datetime.datetime(2018, 5, 3, 0, 0)]

    Keep calm and code in Python, have fun!

    Update 3rd of Jan 2021: previously we also asked for the PyBites N year marks as well, but this unnecessarily complicated this beginner Bite so simplified the requirements a bit.

"""

from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates(dt=PYBITES_BORN):
    while True:
        yield dt + timedelta(days=100)
        dt = dt + timedelta(days=100)
