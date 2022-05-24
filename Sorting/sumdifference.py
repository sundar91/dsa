# Given an integer array, A of size N.
# You have to find all possible non-empty subsequences of the array of numbers and then, for each subsequence, find the difference between the largest and smallest numbers in that subsequence. Then add up all the differences to get the number.

# As the number may be large, output the number modulo 1e9 + 7 (1000000007).

# NOTE: Subsequence can be non-contiguous.


def solve(A):
    mod = pow(10, 9) + 7
    n = len(A)
    A.sort()
    maxSum, minSum = 0, 0
    for i in range(n):
        maxSum += (A[i] * (1 << i)) % mod
        minSum += (A[i] * (1 << (n - i - 1))) % mod

    res = (maxSum - minSum) % mod
    return res
