# You will be given two inputs: a string of words and a letter. For each string, return the alphabetic character after every instance of letter(case insensitive).

# If there is a number, punctuation or underscore following the letter, it should not be returned.

# If letter = 'r':
# comes_after("are you really learning Ruby?") # => "eenu"
# comes_after("Katy Perry is on the radio!")   # => "rya"
# comes_after("Pirates say arrrrrrrrr.")       # => "arrrrrrrr"
# comes_after("r8 your friend")                # => "i"
# Return an empty string if there are no instances of letter in the given string.


def comes_after(st: str, letter: str) -> str:
    res = ""
    for i in range(len(st)):
        if st[i].lower() == letter.lower():
            if i == len(st) - 1:
                break
            if st[i + 1].isalpha():
                res += st[i + 1]
    return res


def comes_after_ol(st: str, letter: str) -> str:
    return "".join(
        y
        for x, y in zip(st, st[1:])
        if x.lower() == letter.lower() and y.isalpha()
    )


if __name__ == "__main__":
    print(comes_after_ol("are you really learning Ruby?", "r"))
    print(comes_after_ol("Katy Perry is on the radio!", "r"))
    print(comes_after_ol("Pirates say arrrrrrrrr.", "r"))
    print(comes_after_ol("r8 your friend", "r"))
