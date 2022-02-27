# Collatz Conjecture
# Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
# Repeat the process until n = 1. It takes a total of steps to reach 1 from n.


counter = 0

# def collatz_conjecture(num : int) -> int:
#     pass


def collatz_conjecture(num):
    global counter
    counter += 1
    stored_num = 0
    if num % 2 == 0:
        stored_num = num / 2
        print("even -- ", stored_num)
    else:
        stored_num = num * 3 + 1
        print("Odd -- ", stored_num)
    if stored_num == 1:
        return
    collatz_conjecture(stored_num)


def collatz_conjecture_while(num: int) -> int:
    counter = 0
    while num > 1:
        if num % 2:
            num = num * 3 + 1
            print("even -- ", num)
        else:
            num //= 2
            print("Odd -- ", num)
        counter += 1
    return counter


print(collatz_conjecture_while(999))
