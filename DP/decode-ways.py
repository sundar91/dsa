class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1

        for i in range(n - 1,  -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                dp[i] += dp[i+2]

        return dp[0]


class Solution2:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [0] * (n + 1)

        if s[0] == '0':
            return 0

        dp[0] = 1

        for i in range(1, n + 1):

            if s[i - 1] != '0':
                dp[i] = dp[i-1]

            if i >= 2:
                twodigit = int(s[i - 2: i])
                if twodigit >= 10 and twodigit <= 26:
                    dp[i] += dp[i - 2]

        return dp[n]


print(Solution2().numDecodings('106'))
