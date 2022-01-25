# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

# Courtesy of projecteuler.net (Problem 1)
# https://projecteuler.net/problem=1


def solution(number):
    if number < 0:
        return 0
    else:
        return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


def solution2(number):
    return sum(set(range(0, number, 3)) | set(range(0, number, 5)))


def solution3(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    print(solution(10))
    print(solution(20))
    print(solution2(200))
    print(solution3(200))
    print(solution3(10))
    print(solution3(20))
    print(solution3(30))
