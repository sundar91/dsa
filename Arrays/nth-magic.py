# Given an integer A, find and return the Ath magic number.

# A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.

# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        pw = 1
        s = 0
        # since power of 5 only counts when bit is set example 
        # 5 (101) -> 5^3 + 5
        while A > 0:
            pw = pw * 5
            if A & 1:
                s += pw
            A = A >> 1
        return s


print(Solution().solve(5))