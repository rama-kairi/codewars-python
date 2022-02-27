# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"


def to_underscore(string: str) -> str:
    """
    Convert PascalCase string to snake_case string
    """
    return "".join(
        f"_{i.lower()}" if k != 0 and i.isupper() else i
        for k, i in enumerate(str(string))
    ).lower()


if __name__ == "__main__":
    print(to_underscore("TestController"))
    print(to_underscore("MoviesAndBooks"))
    print(to_underscore("App7Test"))
    print(to_underscore("1"))
    print(to_underscore(1))
