class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        n = len(A)
        m = len(A[0])
        assert(n >= 1 and n <= 100 and m >= 1 and m <= 100)
        uniquePaths = [[0 for i in range(102)] for j in range(102)]
        for i in range(0, n):
            for j in range(0, m):
                uniquePaths[i][j] = 0
                if (A[i][j]):
                    continue
                if (i == 0 and j == 0):
                    uniquePaths[i][j] = 1
                if (i > 0):
                    uniquePaths[i][j] += uniquePaths[i-1][j]
                if (j > 0):
                    uniquePaths[i][j] += uniquePaths[i][j-1]
        return uniquePaths[n-1][m-1]


print(Solution().uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
