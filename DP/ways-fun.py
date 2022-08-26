# Find the number of ways you can have fun in A days, given you can sleep every day, Pizza can be eaten every alternate day
# and you can watch Tv shows every two days.

# Since the answer could be large, return answer % 109 + 7.


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        mod = int(1e9+7)

        dp = [[0 for _ in range(3)] for _ in range(A + 1)]

        dp[1][0] = dp[1][1] = dp[1][2] = 1

        for i in range(2, A+1):
            # sleep
            dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod

            # pizza
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod

            # TV
            dp[i][2] = (dp[i-1][0] + dp[i-1][1] - 2 * dp[i-2][2] + mod) % mod

        return (dp[A][0] + dp[A][1] + dp[A][2]) % mod
