"""
Bite 5. Parse a list of names

    In this bite you will work with a list of names.

    First you will write a function to take out duplicates and title case them.

    Then you will sort the list in alphabetical descending order by surname and lastly determine what the shortest first name is. For this exercise you can assume there is always one name and one surname.

    With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
"""
from collections import namedtuple

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    titled = [name.title() for name in names]
    return list(dict.fromkeys(titled))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    Name = namedtuple("Name", "full_name first_name last_name")
    names = dedup_and_title_case_names(names)
    Names = [Name(N, N.split()[0], N.split()[1]) for N in names]
    Names_sorted = sorted(Names, key=lambda l: l.last_name, reverse=True)
    return [n.full_name for n in Names_sorted]


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest_name = ""
    shortest_length = 1e9
    firstnames = [name.split()[0] for name in names]
    for firstname in firstnames:
        if len(firstname) < shortest_length:
            shortest_name = firstname
            shortest_length = len(firstname)
    return shortest_name
