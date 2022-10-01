# Problem Description
# You are given a string A consisting of 1's and 0's. Now the task is to make the string consisting of only 1's.
# But you are allowed to perform only the following operation:

# Take exactly B consecutive string elements and change 1 to 0 and 0 to 1.
# Each operation takes 1 unit time, so you have to determine the minimum time required to only make the string of 1's. If not possible, return -1.


class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        temp = [0] * n

        xr = 0
        ans = 0
        i = 0
        while(i <= n - B):
            xr ^= temp[i]
            if((A[i] == '0' and xr == 0) or (A[i] == '1' and xr == 1)):
                ans += 1
                if(i + B < n):
                    temp[i+B] = 1
                xr = 1 - xr
            i += 1

        while(i < n):
            xr ^= temp[i]
            val = ord(A[i]) - 48
            if(val ^ xr == 0):
                return -1
            i += 1

        return ans
