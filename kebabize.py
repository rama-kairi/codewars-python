# Modify the kebabize function so that it converts a camel case string into a kebab case.

# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-humps
# Notes:

# the returned string should only contain lowercase letters
import re


def kababize(s: str) -> str:
    """
    Convert a camel case string into a kebab case string.
    :param s: string
    :return: kebab case string

    >>> kababize('camelsHaveThreeHumps')
    'camels-have-three-humps'
    >>> kababize('camelsHave3Humps')
    'camels-have-humps'
    >>> kababize('SOS')
    's-o-s'
    """
    for k in s:
        if k.isdigit():
            s = s.replace(k, "")

        if k.isupper():
            s = s.replace(k, "-" + k.lower())
    return s.strip("-")


# With comprehension
def kababize_ol(s: str):
    return "".join("-" * i.isupper() + i.lower() * i.isalpha() for i in s).strip("-")


def kababize_re(s: str):
    return "-".join(
        [i for i in re.split("([A-Z][^A-Z]*)", re.sub(r"[^a-zA-Z]", "", s)) if i != ""]
    ).lower()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(kababize_re("camelsHaveThreeHumps"))
    print(kababize_re("camelsHave3Humps"))
    print(kababize_ol("SOS"))
