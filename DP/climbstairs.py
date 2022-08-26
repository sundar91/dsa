class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):

        memo = [-1] * (A + 1)
        mod = 1000000007
        if A <= 2:
            return A

        memo[0] = 0
        memo[1] = 1
        memo[2] = 2

        for i in range(3, A + 1):
            memo[i] = (memo[i-1] + memo[i - 2]) % mod

        return memo[-1]
