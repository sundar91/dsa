# Given an unsorted integer array A of size N.

# Find the length of the longest set of consecutive elements from array A.

# i/p :
# A = [100, 4, 200, 1, 3, 2]
# o/p : 4
# Explanation : The set of consecutive elements will be [1, 2, 3, 4].

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        h = set()
        for i in range(len(A)):
            h.add(A[i])

        ans = 1
        for i in range(len(A)):
            temp = A[i]
            if not (temp - 1) in h:
                count = 0
                while temp in h:
                    count += 1
                    temp += 1
                ans = max(ans, count)
        return ans
