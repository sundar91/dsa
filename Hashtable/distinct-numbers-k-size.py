# You are given an array of N integers, A1, A2 ,…, AN and an integer B. 
# Return the of count of distinct numbers in all windows of size B.

# Formally, return an array of size N-B+1 
# where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

# NOTE: if B > N, return an empty array.

# Example: 
#  A = [1, 2, 1, 3, 4, 3]
#  B = 3

# A=[1, 2, 1, 3, 4, 3] and B = 3
#  All windows of size B are
#  [1, 2, 1]
#  [2, 1, 3]
#  [1, 3, 4]
#  [3, 4, 3]
#  So, we return an array [2, 3, 3, 2].

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
		hashmap = {}
		n = len(A)
		k = n - B + 1
		res = []
		for i in range(B):
			if A[i] in hashmap:
				hashmap[A[i]] += 1
			else:
				hashmap[A[i]] = 1

		res.append(len(hashmap))
		
		for i in range(1, n - B + 1):
			last_index = i + B -1
			if A[last_index] in hashmap:
				hashmap[A[last_index]] += 1
			else:
				hashmap[A[last_index]] = 1
			
			hashmap[A[i-1]] -=1 
			if hashmap[A[i-1]] <= 0:
				hashmap.pop(A[i-1])
			
			res.append(len(hashmap))
		
		return res