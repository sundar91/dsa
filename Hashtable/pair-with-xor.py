
# Given an integer array A containing N distinct integers.
# Find the number of unique pairs of integers in the array whose XOR is equal to B.
# NOTE:
# Pair (a, b) and (b, a) is considered to be the same and should be counted once.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hashset = set()
        count = 0
        for i in range(len(A)):
            rem = A[i] ^ B
            if rem in hashset:
                count += 1

            hashset.add(A[i])
        return count