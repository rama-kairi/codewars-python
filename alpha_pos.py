# // Welcome.

# // In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# // If anything in the text isn't a letter, ignore it and don't return it.

# // "a" = 1, "b" = 2, etc.

# // Example
# // alphabetPosition("The sunset sets at twelve o' clock.")


def alpha_position(text: str) -> str:
    """
    >>> alpha_position("The sunset sets at twelve o' clock.")
    '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'
    >>> alpha_position("The narwhal bacons at midnight.")
    '20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20'
    >>> alpha_position("")
    ''
    """
    return " ".join([str(ord(char) - 96) for char in text.lower() if char.isalpha()])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(alpha_position("The sunset sets at twelve o' clock."))
    print(alpha_position("The narwhal bacons at midnight."))
    print(alpha_position(""))
