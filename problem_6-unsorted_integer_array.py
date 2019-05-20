#!/usr/bin/env python3

import sys

def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    MIN = sys.maxsize
    MAX = - sys.maxsize - 1

    for number in ints:
        if number > MAX:
            MAX = number
        elif number < MIN:
            MIN = number

    return MIN, MAX

## Example Test Case of Ten Integers
import random

# Test Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")

# Test Case 2
l = [3, 2, 5, 7, 3, 2, 1]
random.shuffle(l)

print ("Pass" if ((1, 7) == get_min_max_by_sorting(l)) else "Fail")

# Test Case 3
l = [6, 3, 5, 2, 5, 2, 5]
random.shuffle(l)

print ("Pass" if ((2, 6) == get_min_max_by_sorting(l)) else "Fail")