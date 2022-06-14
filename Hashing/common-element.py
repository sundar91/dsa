# Given two integer array A and B of size N and M respectively. Your task is to find all the common elements in both the array.

# NOTE:

# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        hashmap = {}
        for i in range(n):
            if(hashmap.get(A[i]) == None):
                hashmap[A[i]] = 1
            else:
                hashmap[A[i]] += 1
        
        ans =[] 
        for i in range(m):
            if(hashmap.get(B[i]) != None and hashmap[B[i]] != 0):
                ans.append(B[i])
                hashmap[B[i]] -= 1
            
        return ans