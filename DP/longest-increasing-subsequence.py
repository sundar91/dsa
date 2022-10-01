from re import L
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        lis = [1] * n

        # O(n^2)
        # starting from end and compare all nums afterwards
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)
