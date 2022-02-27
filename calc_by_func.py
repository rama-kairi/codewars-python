# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))


# from typing import Any, Tuple


# def zero(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 0
#     operand, num = c
#     print(f"0{operand}{num}")
#     return eval(f"0{operand}{num}")


# def one(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 1
#     operand, num = c
#     print(operand, num)
#     return eval(f"1{operand}{num}")


# def two(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 2
#     operand, num = c
#     return eval(f"2{operand}{num}")


# def three(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 3
#     operand, num = c
#     return eval(f"3{operand}{num}")


# def four(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 4
#     operand, num = c
#     return eval(f"4{operand}{num}")


# def five(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 5
#     operand, num = c
#     return eval(f"5{operand}{num}")


# def six(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 6
#     operand, num = c
#     return eval(f"6{operand}{num}")


# def seven(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 7
#     operand, num = c
#     print(f"7{operand}{num}")
#     return eval(f"7{operand}{num}")


# def eight(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 8
#     operand, num = c
#     return eval(f"8{operand}{num}")


# def nine(c: Tuple[Any, int] = (None, 0)) -> int:
#     if not c[0]:
#         return 9
#     operand, num = c
#     return eval(f"9{operand}{num}")


# def plus(c: int) -> Tuple[Any, int]:
#     return ("+", c)


# def minus(c: int) -> Tuple[Any, int]:
#     return ("-", c)


# def times(c: int) -> Tuple[Any, int]:
#     print(f"{c=}")
#     return ("*", c)


# def divided_by(c: int) -> Tuple[Any, int]:
#     return ("//", c)


# Second Approach:

# def zero(f=None):
#     return 0 if not f else f(0)


# def one(f=None):
#     return 1 if not f else f(1)


# def two(f=None):
#     return 2 if not f else f(2)


# def three(f=None):
#     return 3 if not f else f(3)


# def four(f=None):
#     return 4 if not f else f(4)


# def five(f=None):
#     return 5 if not f else f(5)


# def six(f=None):
#     return 6 if not f else f(6)


# def seven(f=None):
#     return 7 if not f else f(7)


# def eight(f=None):
#     return 8 if not f else f(8)


# def nine(f=None):
#     return 9 if not f else f(9)


# def plus(y):
#     return lambda x: x + y


# def minus(y):
#     return lambda x: x - y


# def times(y):
#     return lambda x: x * y


# def divided_by(y):
#     return lambda x: x / y


# Third Approach:

# id_ = lambda x: x
# number = lambda x: lambda f=id_: f(x)
# zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
# plus = lambda x: lambda y: y + x
# minus = lambda x: lambda y: y - x
# times = lambda x: lambda y: y * x
# divided_by = lambda x: lambda y: y / x

if __name__ == "__main__":
    print(seven(times(five())))
    print(four(plus(nine())))
    print(eight(minus(three())))
    print(seven(times(zero())))
