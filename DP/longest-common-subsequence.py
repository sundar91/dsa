class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        m = len(B)

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i][j] = 1 + (0 if i == 0 or j == 0 else dp[i-1][j-1])
                else:
                    dp[i][j] = max(
                        0 if i == 0 else dp[i-1][j],
                        0 if j == 0 else dp[i][j-1]
                    )

        return dp[n-1][m-1]
