"""
Bite 8. Rotate string characters

    Write a function that rotates characters in a string, in both directions:

        if n is positive move characters from beginning to end, e.g.: rotate('hello', 2) would return llohe
        if n is negative move characters to the start of the string, e.g.: rotate('hello', -2) would return lohel

    See tests for more info. Have fun!
"""


def rotate(s: str, n: int) -> str:
    """
    Rotate characters in a string.
    Expects string s, and n (int) for number of characters to move.
    """
    if n == 0 or abs(n) >= len(s):
        return s
    else:
        return "".join(list(s)[n:] + list(s)[0:n])
