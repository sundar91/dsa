# Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.

# A-1 mod B is also known as modular multiplicative inverse of A under modulo B.
# formula to solve:
# (A ^ B-1) % B =  1 Fermat Them.
# (A ^ -1) % B = (A ^ B-2) % B

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        p = B - 2
        res = 1
        b = A % B
        while p > 0:
            if p & 1:
                res = (res * b) % B
            p = p >> 1
            b = (b * b) % B

        return res
