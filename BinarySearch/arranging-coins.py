# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        ans = 0
        while l <= r:
            mid = l + ((r - l) // 2)

            nc = (mid * (mid + 1)) // 2

            if nc > n:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1

        return ans
