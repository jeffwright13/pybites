"""
Bite 26. Dictionary comprehensions are awesome

    A dictionary comprehension is like a list comprehension, but it constructs a dict instead of a list. They are convenient to quickly operate on each (key, value) pair of a dict. And often in one line of code, maybe two after checking PEP8 ;)

    We think they are elegant, that's why we want you to know about them!

    In this Bite you are given a dict and a set. Write a dictionary comprehension that filters out the items in the set and returns the resulting dict, so if your dict is {1: 'bob', 2: 'julian', 3: 'tim'} and your set is {2, 3}, the resulting dict would be {1: 'bob'}.

    Check out the tests for more details. Have fun!

    => Comprehensions in Python:
    The comprehension consists of a single expression followed by at least one 'for' clause and zero or more 'for' or 'if' clauses.

    => General template for dictionary comprehension in Python:
    dict_variable = {key:value for (key,value) in dictonary.items()}

"""
input_bites = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
exclude_bites = {6, 10, 16, 18, 21}


def filter_bites_loop(bites=input_bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    ret_dict = {}
    for item in bites.keys():
        if item not in bites_done:
            ret_dict[item] = bites[item]
    return ret_dict


def filter_bites_comprehension(bites=input_bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return {key: value for (key, value) in bites.items() if key not in bites_done}


filter_bites = filter_bites_loop
