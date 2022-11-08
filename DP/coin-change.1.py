class Solution:
    def coinChange(self, coins, amount: int) -> int:

        n = len(coins)
        count = 0

        if amount == 0:
            return 0

        coins.sort()

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[amount]


print(Solution().coinChange([1, 2, 5], 11))
