# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d = {}
        curr_sum = 0
        for x in A:
            curr_sum += x
            # subarray sum can be 0 starting from 0 index
            # if there are duplicates
            if curr_sum == 0 or x == 0 or curr_sum in d:
                return 1
            else:
                d[curr_sum] = 1
        return 0

s = Solution()
print(s.solve([1, 2, 3, 4, 5]))
print(s.solve([1, -1]))