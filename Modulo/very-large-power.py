# Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).

# "^" means power,

# "%" means "mod", and

# "!" means factorial.


# According the Fermat's little
# a(M - 1) = 1 (mod M) if M is a prime.

# So if we rewrite B! as x*(M-1) + y, then the
# task of computing A^ B! becomes A ^ (x*(M-1) + y)
# which can be written as Ax*(M-1)*Ay.
# From Fermat's little theorem, we know Ax*(M-1) = 1.

# What is the value of y?
# From B! = x * (M - 1) + y,
# y can be written as B! % (M-1)

# We can easily use the above theorem such that we can get
# A ^ (B!) % M = (A ^ y ) %  M

# Now we only need to find two things as:-
# 1. y = (B ^ C) % (M - 1)
# 2. Ans = (A ^ y) % M


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1:
            return 1

        f = 1
        mod = pow(10, 9) + 7
        for i in range(2, B + 1):
            f = (f * i) % (mod - 1)

        base = A % mod
        res = 1
        while f > 0:
            if f & 1:
                res = (res * base) % mod

            base = (base * base) % mod
            f = f >> 1

        return res
