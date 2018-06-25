"""
Problem: Write a function merge_ranges which takes a list of tuples
"""

def reverse(list_of_chars, start_idx=0, end_idx=-1):
    """
    Merges ranges into smallest set of continuous ranges
    Time Complexty: O(n)
    Space Complexity: O(1)
    >>> reverse(['a', 'b'])
    ['b', 'a']
    """
    if end_idx == -1:
        end_idx = len(list_of_chars) - 1

    for i in range(start_idx, (end_idx + start_idx) // 2 + 1):
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[end_idx - i + start_idx]
        list_of_chars[end_idx - i + start_idx] = temp

    return list_of_chars




