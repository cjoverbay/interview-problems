"""
Problem: Write a function merge_ranges which takes a list of tuples
"""


def solution_merge_ranges(ranges):
    """
    Merges ranges into smallest set of continuous ranges
    Time Complexty: O(n lg(n))
    Space Complexity: O(n)
    >>> merge_ranges([(1, 2), (4, 6), (5, 7)])
    [(1, 2), (4, 7)]
    """

    sorted_ranges = sorted(ranges[:])

    merged_ranges = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        merge_start, merge_end = merged_ranges[-1]

        if merge_end >= start:
            merged_ranges[-1] = (merge_start, max(end, merge_end))
        else:
            merged_ranges.append((start, end))

    return merged_ranges




