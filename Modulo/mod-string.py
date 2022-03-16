# You are given a large number in the form of a string A where each character denotes a digit of the number.
# You are also given a number B. You have to find out the value of A % B and return it.

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def findMod(self, A, B):
        pw = 1
        n = len(A)
        s = 0
        for i in range(n-1, -1, -1):
            val = int(A[i])
            s += ((val % B) * (pw % B)) % B
            pw = (pw * 10) % B
        return s % B

print(Solution().findMod("43535321", 47))