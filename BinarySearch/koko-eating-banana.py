# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3, 6, 7, 11], h = 8
# Output: 4

import math


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:

        res = max(piles)
        l, r = 1, res

        def search(k):

            t = 0
            for i in range(len(piles)):
                t += math.ceil(piles[i] / k)

            if t > h:
                return False

            return True

        while l <= r:
            mid = l + (r - l) // 2
            val = search(mid)

            if val:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1

        return res


print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))
