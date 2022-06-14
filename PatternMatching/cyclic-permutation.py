# Given two binary strings A and B, count how many cyclic permutations of B when taken XOR with A give 0.

# NOTE: If there is a string, S0, S1, ... Sn-1 , then it is a cyclic permutation is of the form Sk, Sk+1, ... Sn-1, S0, S1, ... Sk-1 where k can be any integer from 0 to N-1.

# since xor of same element is 0, so if we find pattern A in B + B by creating lps (longest prefix suffix)

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)

        s = A + '@' + B + B[0:-1]

        lps = [0] * len(s)

        lps[0] = 0
        for i in range(1, len(s)):
            x = lps[i-1]
            while s[x] != s[i]:
                if x == 0:
                    x = -1
                    break
                x = lps[x - 1]
            lps[i] = x + 1

        count = 0
        for i in range(len(lps)):
            if lps[i] == n:
                count += 1

        return count
