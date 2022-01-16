# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

from functools import reduce
from collections import Counter
from operator import xor


# Easy For Loop way
def find_it(seq: list):
    """
    Given an array of integers, find the one that appears an odd number of times.
    """
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num


# With Python Generator Function
def find_it(seq: list):
    """
    Given an array of integers, find the one that appears an odd number of times.
    """
    return next(num for num in seq if seq.count(num) % 2 != 0)


# With Python List Comprehension
def find_it(seq: list):
    """
    Given an array of integers, find the one that appears an odd number of times.
    """
    return [num for num in seq if seq.count(num) % 2 != 0][0]


# with Python Reduce % operator
def find_it(seq: list):
    """
    Given an array of integers, find the one that appears an odd number of times.
    """
    return reduce(xor, seq)


# with Python Counter
def find_it(seq: list):
    """
    Given an array of integers, find the one that appears an odd number of times.
    """
    return [k for k, v in Counter(seq).items() if v % 2 != 0][0]


# With Lambda Function
def find_it(seq): return [x for x in seq if seq.count(x) % 2 != 0][0]
# find_it = lambda seq: [x for x in seq if seq.count(x) % 2 != 0][0]


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
