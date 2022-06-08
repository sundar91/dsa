# Given three integers A, B, and C, where A represents n, B represents r, and C represents p and p is a prime number greater than equal to n,
# find and return the value of nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p.

# x! means factorial of x i.e. x! = 1 * 2 * 3... * x.

# NOTE: For this problem, we are considering 1 as a prime.

# HINT: This problem can be solved using Fermat’s Little theorem.

# a^p = a (mod p) where p is a prime number.
# a^(p-1) = 1 (mod p)

# Multiply by an inverse on both sides
# a^(p-2) = a^(-1) (mod p).

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        num = den = 1
        if(A == 1 and B == 1 and C == 1):
            return 0
        B = min(B, A - B)
        for i in range(B):
            num = (num * (A - i)) % C
            den = (den * (i + 1)) % C
        return (num * pow(den, C - 2, C)) % C


def pow(A, p, C):
    b = A % C
    r = 1
    while p > 0:
        if p & 1:
            r = (r * b) % C

        p = p >> 1
        b = (b * b) % C

    return r % C
