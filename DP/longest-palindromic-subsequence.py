import sys

sys.setrecursionlimit(10000000)


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        s2 = A[::-1]

        n = len(A)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        return self.lcs(n, n, A, s2, dp)

    def lcs(self, i, j, s1, s2, dp):

        if i == 0 or j == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        if s1[i-1] == s2[j-1]:
            ans = 1 + self.lcs(i-1, j-1, s1, s2, dp)
        else:
            ans = max(self.lcs(i-1, j, s1, s2, dp),
                      self.lcs(i, j-1, s1, s2, dp))

        dp[i][j] = ans
        return ans

# iterative


class Solution2:
    # @param A : string
    # @return an integer
    def solve(self, A):

        s2 = A[::-1]
        n = len(A)
        first, second = [0] * n, [0] * n  # using two 1D arrays
        dp = [[0 for _ in range(n)] for _ in range(n)]  # using 2D array

        for i in range(n):
            for j in range(n):
                if A[i] == s2[j]:
                    dp[i][j] = 1 + (0 if i == 0 or j == 0 else dp[i-1][j-1])
                    second[j] = 1 + (0 if i == 0 or j == 0 else first[j-1])
                else:
                    dp[i][j] = max(
                        0 if i == 0 else dp[i-1][j],
                        0 if j == 0 else dp[i][j-1]
                    )
                    second[j] = max(
                        0 if i == 0 else first[j],
                        0 if j == 0 else second[j-1]
                    )

            first = second.copy()

        return second


print(Solution2().solve('bebeeed'))
