# Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

# Return the count modulo 109 + 7.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        mod = pow(10, 9) + 7
        n = A
        msb = 0
        while n > 1:
            n = n >> 1
            msb += 1

        res = 0
        n = A
        while(n):
            p = (1 << msb)  # previous power
            res += (msb * int(p / 2) + (n - p + 1)) % mod
            n = n & ~(1 << msb)

            while n and msb > 0:
                if n & (1 << msb):
                    break
                msb -= 1

        return res % mod
