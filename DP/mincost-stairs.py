from traceback import print_tb


class Solution:
    def minCostClimbingStairs(self, cost) -> int:

        n = len(cost)
        dp = [-1] * n

        def minCost(i):
            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            res = cost[i] + min(minCost(i + 1),   minCost(i + 2))
            dp[i] = res
            return res

        return minCost(0)


print(Solution().minCostClimbingStairs([10,15,20]))