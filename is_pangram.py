# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string


def is_pangram(s: string) -> bool:
    """
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("The quick brown fox jumps over the lazy cat")
    False
    """
    return set(string.ascii_lowercase) <= set(s.lower())


# With issubset string method
def is_pangram_str(s: string) -> bool:
    """
    >>> is_pangram_str("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram_str("The quick brown fox jumps over the lazy cat")
    False
    """
    return set(string.ascii_lowercase).issubset(set(s.lower()))


# Run tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(is_pangram_str("The quick brown fox jumps over the lazy dog"))
    print(is_pangram_str("The quick brown fox jumps over the lazy cat"))
