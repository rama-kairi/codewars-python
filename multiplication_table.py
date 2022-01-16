# Your task, is to create NxN multiplication table, of size provided in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]


def multiplication_table(num: int) -> list:
    """
    :param num: int
    :return: list
    """
    return [[x * y for y in range(1, num + 1)] for x in range(1, num + 1)]


# Run Tests
if __name__ == "__main__":
    print(multiplication_table(3))  # [[1,2,3],[2,4,6],[3,6,9]]
    print(multiplication_table(4))  # [[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]
    print(multiplication_table(2))  # [[1,2],[2,4]]
    print(multiplication_table(1))  # [[1]]
