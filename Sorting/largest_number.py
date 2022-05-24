# Given an array A of non-negative integers, arrange them such that they form the largest number.

# Note: The result may be very large, so you need to return a string instead of an integer.

# i/p :  A = [3, 30, 34, 5, 9]
# o/p: "9534330"

from functools import cmp_to_key


def compare(A, B):
    if str(A) + str(B) > str(B) + str(A):
        return -1
    if str(A) + str(B) < str(B) + str(A):
        return 1
    return 0


def solve(A):
    A.sort(key=cmp_to_key(compare))
    if A[0] == 0:
        return '0'
    return ''.join([str(n) for n in A])


print(solve([3, 30, 34, 5, 9]))
