# # You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# # Examples
# # [7, 1]  =>  [1, 7]
# # [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_the_odd(arr: list):
    # sort the odd numbers in ascending order
    # while leaving the even numbers at their original positions
    # return the sorted array

    # your code here
    odd_numbers = []
    even_numbers = []
    for i in arr:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    odd_numbers.sort()
    for even in even_numbers:
        odd_numbers.insert(arr.index(even), even)

    return odd_numbers


print(sort_the_odd([7, 1]))
print(sort_the_odd([5, 8, 6, 3, 4]))
print(sort_the_odd([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
