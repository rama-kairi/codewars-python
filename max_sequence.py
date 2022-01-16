# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:


def max_sequence(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maxSequence(arr):
    return max(sum(arr[i:j]) for i in range(len(arr) + 1) for j in range(len(arr) + 1))


print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
