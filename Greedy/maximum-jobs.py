from itertools import count


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        j = []
        for i in range(n):
            j.append((A[i], B[i]))

        j.sort(key=lambda x: x[1])

        count = 0
        prev = 0
        for i in range(n):
            if j[i][0] >= prev:
                count += 1
                prev = j[i][1]

        return count


print(Solution().solve([3, 2, 6], [9, 8, 9]))
