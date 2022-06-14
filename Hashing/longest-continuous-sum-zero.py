# Given an array A of N integers.
# Find the largest continuous sequence in a array which sums to zero.

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):
		n = len(A)
		pf = [0] * n
		
		if n < 1:
			return []

		pf[0] = A[0]
		for i in range(1,n):
			pf[i] = pf[i-1] + A[i]
		
        hashmap = {}
        max_count = 0
        start = -1
		for i in range(n):
            if pf[i] == 0:
                if i + 1 > max_count:
                    start = 0
                    max_count = i + 1 
            elif pf[i] in hashmap:
                temp = i - hashmap[pf[i]]
                if temp > max_count:
                    max_count = temp
                    start = hashmap[pf[i]] + 1
            else:
                hashmap[pf[i]] = i
        
        return A[start: start+max_count]