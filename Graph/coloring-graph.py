class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A <= 3:
            return A

        if A % 2 == 0:
            return 2

        return 3
