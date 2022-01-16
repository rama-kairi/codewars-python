# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

# we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:

# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers.

# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


def dig_pow(num: int, n: int) -> int:
    """
    >>> dig_pow(89, 1)
    1
    >>> dig_pow(92, 1)
    -1
    >>> dig_pow(695, 2)
    2
    >>> dig_pow(46288, 3)
    51
    """
    total = sum(
        int(i) ** j for i, j in zip(list(str(num)), [n + i for i in range(len(list(str(num))))])
    )
    return round(total / num) if total % num == 0 else -1


# With Onl line
def dig_pow(num: int, n: int) -> int:
    return round(sum(int(i) ** (n + i) for i, j in enumerate(list(str(num)))) / num)


# Run tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(695, 2))
    print(dig_pow(46288, 3))
