
# Bottom up
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[n][m] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and s1[i] == s3[i + j] and dp[i+1][j]:
                    dp[i][j] = True

                if j < n and s2[j] == s3[i+j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]

# Top down


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        n = len(s1)
        m = len(s2)
        #k = i + j

        def dfs(i, j, k):

            if i >= n and j >= m:
                return True

            # if k >= len(s3):
            #     return False

            if (i, j) in cache:
                return cache[(i, j)]

            if i < n and s1[i] == s3[i + j] and dfs(i+1, j):
                return True

            if j < n and s2[j] == s3[i+j] and dfs(i, j + 1):
                return True

            cache[(i, j)] = False

            return False

        return dfs(0, 0, 0)


print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbbcbcac'))
