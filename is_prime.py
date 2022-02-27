# Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.
# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */


# Version 1
def is_prime_v1(num: int) -> bool:
    """
    Return True if num is a prime number, False otherwise.
    """
    return False if num < 2 else all(num % i != 0 for i in range(2, num))


# Version 2
def is_prime_v2(num: int) -> bool:
    import math

    """
    Return True if num is a prime number, False otherwise.
    """
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, math.floor(math.sqrt(num)) + 1))


# Version 3
def is_prime_v3(num: int) -> bool:
    """
    Return True if num is a prime number, False otherwise.
    """
    import math

    # if its even and not 2, its not a prime
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0 and num > 2:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


# Version 4
def is_prime_v4(num: int) -> bool:
    """
    Return True if num is a prime number, False otherwise.
    """
    return num > 1 and all(num % i for i in range(2, int(num ** 0.5 + 1)))


if __name__ == "__main__":
    import timeit

    # print(
    #     timeit.timeit(
    #         "is_prime_v1(5099)", setup="from __main__ import is_prime_v1", number=100000
    #     )
    # )

    print(
        timeit.timeit(
            "is_prime_v2(5099)", setup="from __main__ import is_prime_v2", number=100000
        )
    )

    print(
        timeit.timeit(
            "is_prime_v3(5099)", setup="from __main__ import is_prime_v3", number=100000
        )
    )

    print(
        timeit.timeit(
            "is_prime_v4(5099)", setup="from __main__ import is_prime_v4", number=100000
        )
    )
