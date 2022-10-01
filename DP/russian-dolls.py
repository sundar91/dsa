class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda x: x[0])

        n = len(A)
        lis = [1] * n

        # calculating lis
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if A[i][0] < A[j][0] and A[i][1] < A[j][1]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)


t = [
    [5, 4],
    [6, 4],
    [6, 7],
    [2, 3]
]


print(Solution().solve(t))
