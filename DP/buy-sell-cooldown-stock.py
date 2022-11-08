class Solution:
    def maxProfit(self, prices) -> int:

        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        n = len(prices)

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, isBuying):
            if i >= n:
                return 0

            if (i, isBuying) in dp:
                return dp[(i, isBuying)]

            ans = dfs(i + 1, True)
            if isBuying:
                ans = max(dfs(i + 1, False) - prices[i], ans)
            else:
                ans = max(dfs(i + 2, True) + prices[i], ans)

            dp[(i, isBuying)] = ans
            return ans

        return dfs(0, True)


print(Solution().maxProfit([1, 2, 3, 0, 2]))
