# Given an array of integers A of size N containing GCD of every possible pair of elements of another array.

# Find and return the original numbers used to calculate the GCD array in any order.
# For example, if original numbers are {2, 8, 10} then the given array will be {2, 2, 2, 2, 8, 2, 2, 2, 10}.

import math


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort(reverse=True)
        n = len(A)
        res = []
        h = {}

        for i in range(n):
            if h.get(A[i], 0) > 0:
                h[A[i]] -= 1
            else:
                for j in range(len(res)):
                    g = self.gcd(A[i], res[j])
                    h[g] = 2 + h.get(g, 0)

                res.append(A[i])

        return res

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


# Sliding window
# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
#         n = len(A)
#         window = int(math.sqrt(n))
#         res = [0] * window
#         maxVal, count, k  = 0, 0, 0

#         for i in range(n):
#             if A[i] > maxVal:
#                 maxVal = A[i]

#             count += 1
#             if window == count:
#                 res[k] = maxVal
#                 k += 1
#                 count = 0
#                 maxVal = 0

#         res.sort()
#         return res
