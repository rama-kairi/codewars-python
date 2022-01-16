# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


def character_occurrence(string: str) -> dict:
    """
    Counts all the occurring characters in a string.
    :param string: string to be analyzed
    :return: dictionary with characters and their occurrences
    """
    return {char: string.count(char) for char in string} if string else {}


if __name__ == "__main__":
    print(character_occurrence("aba"))
    print(character_occurrence("aba"))
    print(character_occurrence(""))
