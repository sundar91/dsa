class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def isMatch(self, A, B):

        n = len(A)
        m = len(B)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        dp[0][0] = True

        for i in range(1, m + 1):
            if B[i-1] == "*":
                dp[0][i] = True
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if B[j - 1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif B[j-1] == "*":
                    # remove * from B and a character from A
                    # remove single character form A
                    # remove * from B
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    if B[j-1] == A[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False

        # print(dp)
        return int(dp[n][m])


print(Solution().isMatch('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '***'))
print(Solution().isMatch('cc', '***??'))
print(Solution().isMatch('cacbcab', 'c*bb?*b?'))
print(Solution().isMatch('bcaccbabaa', 'bb*c?c*?'))
