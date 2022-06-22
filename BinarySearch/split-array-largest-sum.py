# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.


class Solution:
    def splitArray(self, nums, m) -> int:
        def checkSum(target):
            count = 0
            s = 0
            for num in nums:
                s += num
                if s > target:
                    s = num
                    count += 1
            return count + 1 <= m

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l)//2)
            if checkSum(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
