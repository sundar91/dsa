# You are given a number A in the form of a string. Check if the number is divisible by 8 or not.
# Return 1 if it is divisible by eight else, return 0.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        pw = 1
        n = len(A)
        s = 0
        for i in range(n-1, -1, -1):
            val = int(A[i])
            s += ((val % 8) *  (pw % 8)) % 8 
            pw = (pw * 10) % 8
        
        if s % 8 == 0:
            return 1
        else:
            return 0

print(Solution().solve('16'))