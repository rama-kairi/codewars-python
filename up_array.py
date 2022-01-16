# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.

# Examples
# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

# [4, 3, 2, 5] would return [4, 3, 2, 6]


def up_array(arr: list) -> list:
    """
    Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
    >>> up_array([2, 3, 9])
    [2, 4, 0]
    >>> up_array([4, 3, 2, 5])
    [4, 3, 2, 6]
    >>> up_array([]) is None
    True
    >>> up_array([1, -9]) is None
    True
    """
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]


# With Oneline
def up_array_ol(arr):
    return (
        None
        if arr == [] or any(x not in range(10) for x in arr)
        else [int(c) for c in str(int("".join([str(x) for x in arr])) + 1)]
    )


def up_array_an(arr):
    if arr and all(0 <= v <= 9 for v in arr):
        return list(map(int, str(int("".join(map(str, arr))) + 1)))


up_array_lambda = (
    lambda arr: None
    if len(arr) == 0 or any(n < 0 or n > 9 for n in arr)
    else list(map(int, str(int("".join(map(str, arr))) + 1)))
)


# Run Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(up_array_lambda([2, 3, 9]))
    print(up_array_lambda([4, 3, 2, 5]))
    print(up_array_lambda([]))
    print(up_array_lambda([1, -9]))
