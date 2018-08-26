"""
Problem: Write a function which will merge two sorted lists
"""

def merge_sorted_lists(list1, list2):
    """
    Merges two lists
    Time Complexty: O(n)
    Space Complexity: O(n)

    >>> merge_sorted_lists([-1, 0, 3, 4], [-2, 2])
    [-2, -1, 0, 2, 3, 4]
    """
    len_a = len(list1)
    len_b = len(list2)

    n = len_a + len_b

    merged = [0] * n
    a = 0
    b = 0

    for i in range(n):
        if a >= len_a:
            merged[i] = list2[b]
            b += 1
        elif b >= len_b or list1[a] < list2[b]:
            merged[i] = list1[a]
            a += 1
        else:
            merged[i] = list2[b]
            b += 1

    return merged
