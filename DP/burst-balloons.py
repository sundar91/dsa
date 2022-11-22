class Solution:
    def maxCoins(self, nums) -> int:

        nums = [1] + nums + [1]

        cache = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            cache[(l, r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r + 1]
                coins += dfs(i+1, r) + dfs(l, i-1)  # right + left
                cache[(l, r)] = max(coins, cache[(l, r)])
            return cache[(l, r)]

        return dfs(1, len(nums) - 2)


class Solution2:
    def maxCoins(self, nums) -> int:

        n = len(nums)
        nums = [1] + nums + [1]

        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i > j:
                    continue

                dp[i][j] = 0
                for k in range(i, j + 1):
                    coins = nums[i-1] * nums[k] * nums[j+1]
                    coins += dp[i][k-1] + dp[k+1][j]
                    dp[i][j] = max(coins, dp[i][j])

        print(dp)
        return dp[1][n]


print(Solution2().maxCoins([3, 1, 5, 8]))
