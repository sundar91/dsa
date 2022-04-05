class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def LCM(self, A, B):
        gcd = self.GCD(A,B)
        lcm = int((A * B)/ gcd)
        return lcm 

    def GCD(self, A, B):
        if A == 0:
            return B        
        return self.GCD(B % A, A)

# lcm * gcd = a * b