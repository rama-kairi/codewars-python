# Write a function called repeatStr which repeats the given string string exactly n times.

# repeatStr(6, "I") // "IIIIII"
# repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"


def repeat_str(repeat: int, string: str) -> str:
    return "".join(string for _ in range(repeat))


def repeat_str_2(repeat: int, string: str) -> str:
    return string * repeat


if __name__ == "__main__":
    print(repeat_str_2(6, "I"))
    print(repeat_str_2(5, "Hello"))
