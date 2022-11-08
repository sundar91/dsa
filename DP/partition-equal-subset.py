# Given a non-empty array nums containing only positive integers,
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

class Solution:
    # O(n * sums(n))
    def canPartition(self, nums) -> bool:

        s = sum(nums)

        if s % 2:
            return False

        target = s // 2
        n = len(nums)

        def dfs(i, t):
            if t == 0:
                return True

            if i >= n:
                return False

            # include
            return dfs(i+1, t - nums[i]) or dfs(i+1, t)

        return dfs(0, target)


class Solution2:
    def canPartition(self, nums) -> bool:

        s = sum(nums)

        if s % 2:
            return False

        n = len(nums)

        dp = set()
        dp.add(0)
        target = s // 2

        for i in range(n-1, -1, -1):
            temp = set()
            for t in dp:
                temp.add(t)
                temp.add(t + nums[i])
            
            dp = temp
            if target in dp:
                return True
        
        return False
            



     

print(Solution().canPartition([1, 2, 3, 5]))
