import sys

sys.setrecursionlimit(10000)


class Solution:
    # @param A : integer
    # @return an integer
    def __init__(self):
        self.dp = []

    def solve(self, A):
        self.dp = [-1] * (A + 1)

        self.calc(A)
        return self.dp[A]

    def calc(self, A):
        if A <= 1:
            return A

        if self.dp[A] != -1:
            return self.dp[A]

        ans = 0
        for i in range(1, 6):

            if i == A:
                ans += 1
                break

            a = self.calc(A - i)
            ans += a

        self.dp[A] = ans
        return ans


# iterative
class Solution2:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dp = [0 for i in range(A + 1)]
        dp[0] = 1
        mod = 1000000007
        for i in range(1, A+1):
            dp[i] = 0
            for j in range(1, 7):
                if i >= j:
                    dp[i] = (dp[i] + dp[i - j]) % mod

        return dp[A]


print(Solution().solve(4))
