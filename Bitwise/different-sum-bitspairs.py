# We define f(X, Y) as the number of different corresponding bits in the binary representation of X and Y.
# For example, f(2, 7) = 2, since the binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.

# You are given an array of N positive integers, A1, A2,..., AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.

class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        ans = 0
        if(len(A) > 100000):
            return -1
        for b in range(31):
            c0, c1 = 0, 0
            for i in A:
                if i & (1 << b):
                    c1 += 1
                else:
                    c0 += 1
            ans += 2 * c1 * c0
            ans %= (1000000007)
        return ans
