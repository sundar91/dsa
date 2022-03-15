class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
         m = len(A)
         n = len(B)
         p = max(m,n)
         carry = 0
         res = ""
         i = m - 1
         j = n -1 
         while i >= 0 or j >=0:
             first = 0
             second = 0
             if i >= 0:
                 first = int(A[i])
             if j >= 0:
                 second = int(B[j])
             
             s = first + second + carry
             rem = s % 2
             res = str(rem) + res
             carry = int(s / 2)  
             i -= 1
             j -= 1 
         return res