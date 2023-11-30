#!/usr/bin/python3
"""Finds peak in a list of ints, interview prep
"""

"""
    THOUGHT PROCESS
        Not yet sorted hence sorting would take n(log(n))
            -> sorting not worthy
        looping and tracking the max (brute force)
            -> O(n)

        Reducing the run time by 1/2 possibly looping from each end
            -> still O(n)
"""


def find_peak(list_of_integers):
    """Implementing BRUTE force for question
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
