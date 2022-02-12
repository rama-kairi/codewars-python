# Write a function that takes a number as range and returns a list of strings with the following rules:
# if the number is divisible by 3, the list has one item: "Fizz"
# if the number is divisible by 5, the list has one item: "Buzz"
# if the number is divisible by both 3 and 5, the list has two items: "FizzBuzz"
# if the number is not divisible by 3 or 5, the list has one item: the number, formatted as a string

# Input: fizz_buzz(15)
# Output: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

# def fizz_buzz(n: int) -> list:
#     pass


def fizz_buzz(n: int) -> list:
    return [
        "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)
        for n in range(1, n + 1)
    ]


if __name__ == "__main__":
    print(fizz_buzz(15))


def fizz_buzz_new(n: int) -> list:
    return [
        "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)
        for n in range(1, n + 1)
    ]
