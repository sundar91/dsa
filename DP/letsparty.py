# In Danceland, one person can party either alone or can pair up with another person.

# Can you find in how many ways they can party if there are A people in Danceland?

# Note: Return your answer modulo 10003, as the answer can be large.

# N = 4
# output = 4
#  Let suppose three people are A, B, and C. There are only 4 ways to party
#  (A, B, C) All party alone
#  (AB, C) A and B party together and C party alone
#  (AC, B) A and C party together and B party alone
#  (BC, A) B and C party together and A
#  here 4 % 10003 = 4, so answer is 4.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A <= 2:
            return A

        dp = [0] * (A + 1)  # array to store values of subproblems
        mod = 10003

        # intialize base conditions
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, A + 1):
            # alone + pair
            dp[i] = (dp[i - 1] + (i - 1) % mod * dp[i - 2] % mod) % mod
            # solve sub problems
            # taking mod to prevent overflow

        return dp[A]  # return answer
