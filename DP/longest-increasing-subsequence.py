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

        print(lis)
        return max(lis)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:

        lis = []

        def search(val):
            l, r = 0, len(lis) - 1

            ans = -1
            while l <= r:
                mid = l + (r - l) // 2

                if lis[mid] < val:
                    l = mid + 1
                elif lis[mid] >= val:
                    ans = mid
                    r = mid - 1
            return ans

        n = len(nums)
        if n == 0:
            return 0

        for n in nums:
            index = search(n)
            if index == -1:
                lis.append(n)
            else:
                lis[index] = n

        return len(lis)


print(Solution2().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
