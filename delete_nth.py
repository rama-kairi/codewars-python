# Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

# Task
# Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

# Example
#   delete_nth ([1,1,1,1],2) # return [1,1]

#   delete_nth ([20,37,20,21],1) # return [20,37,21]


def delete_nth(arr: list, n: int) -> list:
    """
    >>> delete_nth([1,1,1,1],2)
    [1, 1]
    >>> delete_nth([20,37,20,21],1)
    [20, 37, 21]
    """
    return [x for i, x in enumerate(arr) if arr[:i].count(x) < n]
    # for i, x in enumerate(arr):
    #     print(arr[:i], arr[:i].count(x), x)


from collections import Counter

# def delete_nth(order, max_e):
#     c = Counter()
#     res = []
#     for el in order:
#         if c[el] < max_e:
#             c[el] += 1
#             res.append(el)

#     return res


# def delete_nth(arr: list, n: int) -> list:
#     """
#     >>> delete_nth([1,1,1,1],2)
#     [1, 1]
#     >>> delete_nth([20,37,20,21],1)
#     [20, 37, 21]
#     """
#     ans = []
#     for o in arr:
#         if ans.count(o) < n:
#             ans.append(o)
#     return ans


# With One Line
def delete_nth_ol(arr: list, n: int) -> list:
    """
    >>> delete_nth([1,1,1,1],2)
    [1, 1]
    >>> delete_nth([20,37,20,21],1)
    [20, 37, 21]
    """
    return [o for i, o in enumerate(arr) if arr[:i].count(o) < n]


# Tests
if __name__ == "__main__":
    # import doctest

    # doctest.testmod()
    # print(delete_nth([1, 1, 1, 1], 2))
    print(delete_nth([20, 37, 20, 21, 21, 21, 21, 21, 21], 4))
    # print(delete_nth([20, 20, 21, 33], 1))
    # print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
    # print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 3))
    # print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 1))
