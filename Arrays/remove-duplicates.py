class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if nums.length == 0: 
            return 0

        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1


print(Solution().removeDuplicates([1,1]))
