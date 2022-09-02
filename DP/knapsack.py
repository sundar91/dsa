class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        n = len(A)
        dp = [0] * (C+1)
        for i in range(n):
            for j in range(C, -1, -1):
                dp[j] = dp[j]

                if j >= B[i]:
                    dp[j] = max(dp[j], A[i] + dp[j - B[i]])
            print(dp)

        return dp[C]


print(Solution().solve([2, 4], [19, 48], 41))
