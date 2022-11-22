# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.


# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = {}

        def dfs(i, j):
            if i == n and j == m:
                return 1

            if i >= n or j >= m:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            ans = 0
            if s[i] == t[j]:
                ans = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                ans = dfs(i+1, j)

            dp[(i, j)] = ans
            return ans

        return dfs(0, 0)


class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]


print(Solution().numDistinct("rabbbit", "rabbit"))
