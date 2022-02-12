# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

# For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

# For your convenience, the input is formatted such that a space is provided between every token.

# Empty expression should evaluate to 0.

# Valid operations are +, -, *, /.

# You may assume that there won't be exceptional situations (like stack underflow or division by zero).


def calc(inp: str) -> float:
    if not inp:
        return 0
    stack = []
    for token in inp.split():
        if token in "+-*/":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(str(eval(f"{op1}{token}{op2}")))
        else:
            stack.append(token)
    return float(stack[0])


if __name__ == "__main__":
    print(calc("5 1 2 + 4 * + 3 -"))
    print(calc(""))
    print(calc("3"))
    print(calc("3.5"))
