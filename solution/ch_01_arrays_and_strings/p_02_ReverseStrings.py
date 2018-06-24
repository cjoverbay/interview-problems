"""
Problem: Write a function merge_ranges which takes a list of tuples
"""


def reverse_string(s):
    return ''.join(reverse([c for c in s]))

def reverse(list_of_chars):
    """
    Merges ranges into smallest set of continuous ranges
    Time Complexty: O(n)
    Space Complexity: O(1)
    >>> all_unique(['a', 'b'])
    ['b', 'a']
    """

    for i in range(len(list_of_chars)/2):
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[-(i+1)]
        list_of_chars[-(i+1)] = temp

    return list_of_chars




