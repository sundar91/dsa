
# recursive
class Solution:
    def __init__(self):
        self.dp = []

    def solve(self, A):
        n = len(A)
        self.dp = [[-1 for i in range(n)] for _ in range(n)]

        return self.mincost(A, 0, n-2)

    def mincost(self, A, i, j):

        if i == j:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        ans = float('inf')
        for k in range(i, j):
            ans = min(ans, self.mincost(A, i, k) +
                      self.mincost(A, k+1, j) + A[i] * A[k+1] * A[j+1])

        self.dp[i][j] = ans
        return ans

# iterative


class Solution2:
    def solve(self, A):
        n = len(A)
        dp = [[0 for i in range(n)] for _ in range(n)]

        for l in range(2, n):
            for start in range(1, n - l + 1):
                end = start + l - 1
                if start == end:
                    continue

                ans = float('inf')
                for k in range(start, end):
                    ans = min(ans, dp[start][k] + dp[k+1]
                              [end] + A[start-1] * A[k] * A[end])

                dp[start][end] = ans

        return dp[1][n-1]


print(Solution2().solve([10, 20, 30]))
