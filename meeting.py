# John has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
# Could you make a program that

# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
# It can happen that in two distinct families with the same family name two people have the same first name too.

# Notes
# You can see another examples in the "Sample tests".
import re


def meeting(names: str):
    return "".join(
        f"({a}, {b})"
        for a, b in sorted(name.split(":")[::-1] for name in names.upper().split(";"))
    )


def meeting_ol(s):
    return "".join(
        f"({a}, {b})" for a, b in sorted(name.split(":")[::-1] for name in s.upper().split(";"))
    )


# With Regular Expressions
# def meeting_re(s):
#     return "".join(
#         f"({a}, {b})" for a, b in sorted(re.split(r"[:;]", name) for name in s.upper().split(";"))
#     )


if __name__ == "__main__":
    print(
        meeting_ol(
            "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
        )
    )
    print(
        meeting_ol(
            "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
        )
    )
