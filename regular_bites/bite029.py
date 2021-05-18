"""
Bite 29. Martin's IQ test

    Martin is preparing to pass an IQ test.

    The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being alphanumeric or not.

    Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.

    Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

    Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

    Examples:

    ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
    ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
"""
alphanums = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_index_different_char(chars):
    num_alphas = 0
    num_non_alphas = 0

    for i in range(len(chars)):
        if str(chars[i]) in alphanums:
            num_alphas += 1
        else:
            num_non_alphas += 1

        if (num_alphas >= 1 and str(chars[i]) not in alphanums) or (
            num_non_alphas >= 1 and str(chars[i]) in alphanums
        ):
            return i
