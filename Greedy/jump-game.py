# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Brute Force
class Solution2:
    def canJump(self, nums) -> bool:
        n = len(nums)

        def dfs(i):
            if i == n-1:
                return True

            if nums[i] == 0:
                return False

            res = False
            for j in range(1, nums[i] + 1):
                res = dfs(i + j)
                if res:
                    return True

            return res

        return dfs(0)


class Solution:
    def canJump(self, nums) -> bool:

        n = len(nums)
        target = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= target:
                target = i

        return True if target == 0 else False


print(Solution().canJump([0]))
