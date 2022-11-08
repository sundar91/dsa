# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down.
# You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = {}  # [[-1 for _ in range(m)] for _ in range(n)]

        def dfs(r, c, prevVal):
            if r < 0 or r == n or c < 0 or c == m or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        res = float('-inf')
        for i in range(n):
            for j in range(m):
                r = dfs(i, j, -1)
                res = max(res, r)

        return res


print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
print(Solution().longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
