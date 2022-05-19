# Given three integers A, B, and C, where A represents n, B represents r, and C represents m, 
# find and return the value of nCr % m where nCr % m = (n!/((n-r)!*r!))% m.

# x! means factorial of x i.e. x! = 1 * 2 * 3... * x.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = [[0 for i in range(B + 1)] for j in range(A + 1)]
        for i in range(A + 1):
            for j in range(min(i, B) + 1):
                if(j == i or j == 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % C
        return (dp[A][B] % C)