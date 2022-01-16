# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]
# FUNDAMENTALSARRAYS
import re


# With List Comprehension
def array_diff(arr1: list, arr2: list) -> list:
    return [x for x in arr1 if x not in arr2]


# With filter higher order function
def array_diff_filter(arr1: list, arr2: list) -> list:
    return list(filter(lambda x: x not in arr2, arr1))


# Tests
if __name__ == "__main__":
    print(array_diff_filter([1, 2], [1]))
    print(array_diff_filter([1, 2, 2], [1]))
    print(array_diff_filter([1, 2, 2, 2, 3], [2]))
