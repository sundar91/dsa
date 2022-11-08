class Solution:
    def uniquePaths(self, m: int, n: int):

        current, prev = [0] * m, [0] * m
        current[0] = 1

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                current[j] = prev[j] + (0 if (j-1) < 0 else current[j-1])
                prev = current

        return current[m-1]


print(Solution().uniquePaths(3, 2))
