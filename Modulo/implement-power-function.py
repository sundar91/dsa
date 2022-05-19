# Implement pow(A, B) % C.
# In other words, given A, B and C, Find (A^B % C).
# Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0:
            return 0

        p = 1
        b = A % C
        while B > 0:
            if B & 1:  # odd
                p = (p * b) % C

            B = B >> 1
            b = (b * b) % C

        return p % C


# Recursive Approach
class Solution2:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0:
            return 0

        if B == 0:
            return 1

        p = self.pow(A, int(B/2), C) % C
        p = (p * p) % C
        if B & 1:  # odd
            return (A * p) % C
        return p
