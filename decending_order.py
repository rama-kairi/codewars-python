# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321


def descending_order(num: int):
    return int("".join(sorted(str(num), reverse=True)))


if __name__ == "__main__":
    print(descending_order(42145))
    print(descending_order(145263))
    print(descending_order(123456789))
