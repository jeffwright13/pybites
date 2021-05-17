import bite026

TEST_DICT = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
TEST_SET_1 = (1, 3, 5)
TEST_SET_2 = ("a", "c", "e")
TEST_SET_3 = ()
TEST_SET_4 = set(TEST_DICT.keys())


def test_input_set_not_empty_but_has_no_matching_items():
    assert bite026.filter_bites(TEST_DICT, TEST_SET_1) == TEST_DICT
    assert bite026.filter_bites_comprehension(TEST_DICT, TEST_SET_1) == TEST_DICT


def test_input_set_has_some_values_in_input_dict():
    assert bite026.filter_bites(TEST_DICT, TEST_SET_2) == {"b": 2, "d": 4}
    assert bite026.filter_bites_comprehension(TEST_DICT, TEST_SET_2) == {"b": 2, "d": 4}


def test_input_set_is_empty():
    assert bite026.filter_bites(TEST_DICT, TEST_SET_3) == TEST_DICT
    assert bite026.filter_bites_comprehension(TEST_DICT, TEST_SET_3) == TEST_DICT


def test_input_set_has_same_keys_as_input_dict():
    assert bite026.filter_bites(TEST_DICT, TEST_SET_4) == {}
    assert bite026.filter_bites_comprehension(TEST_DICT, TEST_SET_4) == {}


def test_input_bites():
    assert bite026.filter_bites(bite026.input_bites, bite026.exclude_bites) == {
        7: "Parsing dates from logs",
        9: "Palindromes",
        11: "Enrich a class with dunder methods",
        12: "Write a user validation function",
        13: "Convert dict in namedtuple/json",
        14: "Generate a table of n sequences",
        15: "Enumerate 2 sequences",
        17: "Form teams from a group of friends",
        19: "Write a simple property",
        20: "Write a context manager",
    }
    assert bite026.filter_bites_comprehension(
        bite026.input_bites, bite026.exclude_bites
    ) == {
        7: "Parsing dates from logs",
        9: "Palindromes",
        11: "Enrich a class with dunder methods",
        12: "Write a user validation function",
        13: "Convert dict in namedtuple/json",
        14: "Generate a table of n sequences",
        15: "Enumerate 2 sequences",
        17: "Form teams from a group of friends",
        19: "Write a simple property",
        20: "Write a context manager",
    }
