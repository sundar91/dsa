# Problem Description
# Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

# More formally,

# G[i] for an element A[i] = an element A[j] such that

# j is maximum possible AND

# j < i AND

# A[j] < A[i]

# Elements for which no smaller element exist, consider the next smaller element as -1.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        nsl = [-1] * n
        stck = []
        for i in range(n):
            val = A[i]
            while len(stck) > 0 and stck[-1] >= val:
                stck.pop()

            if len(stck) == 0:
                nsl[i] = -1
            else:
                nsl[i] = stck[-1]

            stck.append(val)

        return nsl
