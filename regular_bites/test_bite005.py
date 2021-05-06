import bite005
import pytest


@pytest.mark.parametrize(
    "name_list, expected",
    [
        (
            ["fred flintstone", "barney rubble", "cheeto degaul"],
            ["Fred Flintstone", "Barney Rubble", "Cheeto Degaul"],
        ),
        (
            ["fred flintstone", "fred flintstone", "barney rubble", "cheeto degaul"],
            ["Fred Flintstone", "Barney Rubble", "Cheeto Degaul"],
        ),
    ],
)
def test_dedup_and_title_case_names(name_list, expected):
    assert bite005.dedup_and_title_case_names(name_list) == expected


@pytest.mark.parametrize(
    "name_list, expected",
    [
        (
            ["Fred Flintstone", "Barney Rubble", "Cheeto Degaul"],
            ["Barney Rubble", "Fred Flintstone", "Cheeto Degaul"],
        ),
    ],
)
def test_sort_by_surname_desc(name_list, expected):
    assert bite005.sort_by_surname_desc(name_list) == expected


def test_shortest_first_name():
    assert bite005.shortest_first_name(bite005.NAMES) == "Al"
