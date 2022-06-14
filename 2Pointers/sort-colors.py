# Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

# HINT : Put all 0's at start and 2's at end.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        n = len(A)
        i, j, k = 0, n - 1, n - 1

        while i < k:

            if A[i] == 0:
                i += 1
                continue

            if A[i] == 1:
                if i < j:
                    A[i], A[j] = A[j], A[i]
                    j -= 1
                    continue
                else:
                    i += 1
            else:
                A[i], A[k] = A[k], A[i]
                k -= 1
                if j > k:
                    j = k

        return A
