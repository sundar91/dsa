class Solution:
    def maxProduct(self, nums) -> int:

        res = max(nums)

        cmax, cmin = 1, 1

        for num in nums:

            if num == 0:
                cmax = cmin = 1
                continue

            t = num * cmax
            # maintain max and min at each index
            cmax = max(num * cmax, num * cmin, num)
            cmin = min(t, num * cmin, num)
            res = max(res, cmax)

        return res


print(Solution().maxProduct([-2, 0, -1, 2, 5]))
