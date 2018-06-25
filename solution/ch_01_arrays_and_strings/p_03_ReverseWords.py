"""
Problem: Write a function merge_ranges which takes a list of tuples
"""
from solution.ch_01_arrays_and_strings import p_02_ReverseStrings


def reverse_words(list_of_chars, delimiter=' '):
    """
    Merges ranges into smallest set of continuous ranges
    Time Complexty: O(n)
    Space Complexity: O(1)
    >>> reverse_words(['a', 'b', ' ', 'c'])
    ['c', ' ', 'a', 'b']
    """
    word_start = 0

    for i in range(len(list_of_chars)):
        if i == len(list_of_chars) - 1 or list_of_chars[i+1] == delimiter:
            # reverse each word
            p_02_ReverseStrings.reverse(list_of_chars, word_start, i)
            word_start = i + 2

    # reverse whole string
    return p_02_ReverseStrings.reverse(list_of_chars)
