class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)

        cache = {}

        def dfs(i, j):

            if i >= n and j >= m:
                return True

            if j >= m:
                return False

            if (i, j) in cache:
                return cache[(i, j)]

            match = i < n and (s[i] == p[j] or p[j] == '.')

            cache[(i, j)] = False
            if (j + 1) < m and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)

            return cache[(i, j)]

        return dfs(0, 0)


print(Solution().isMatch("aab", "c*a*b"))
