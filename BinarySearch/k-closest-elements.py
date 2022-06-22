# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]


# O (log(n- k) + k)

class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        l, r = 0, n - k
        while l < r:
            mid = l + ((r-l) // 2)

            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:l + k]
