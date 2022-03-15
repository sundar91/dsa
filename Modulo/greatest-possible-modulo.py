# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.



class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return abs(A-B)


print(Solution().solve(5, 10))

# hint : observe that the maximum value equals the absolute difference between A and B.