# You are given three positive integers, A, B, and C.

# Any positive integer is magical if divisible by either B or C.

# Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

# i/p :
#  A = 4
#  B = 2
#  C = 3
# o/p : 6
# Explanation => 2, 3, 4, 6

def computeGCD(x, y):
    while y:
        x, y = y, x % y

    return x


mod = 1000000007


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        global mod
        low = 2
        high = 1000000000000000000
        ans = 0
        a = B
        b = C
        lc = (a * b) // computeGCD(a, b)
        while low <= high:
            mid = low + (high - low) // 2
            ct = mid // a + mid // b - mid // lc
            if ct >= A:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        ans %= mod
        return ans
