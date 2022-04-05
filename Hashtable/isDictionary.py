
# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. 
# The order of the alphabet is some permutation of lowercase letters.

# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, 
# return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

# Examples: 

# Input 1:

#  A = ["hello", "scaler", "interviewbit"]
#  B = "adhbcfegskjlponmirqtxwuvzy"

#  Output -> 1
#   The order shown in string B is: h < s < i for the given words. So return 1.

# Input 2:

#  A = ["fine", "none", "no"]
#  B = "qwertyuiopasdfghjklzxcvbnm"

#  Output -> 0
#   "none" should be present after "no". Return 0.

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        hashmap = {}
        for i in range(len(B)):
            hashmap[B[i]] = i
        
        s = A[0]
        
        for i in range(1, len(A)):
            cs = A[i]
            j = 0
            while j < len(cs) and j < len(s):
                prev = s[j]
                current = cs[j]
                if hashmap[prev] < hashmap[current]:
                    break;
                    
                if hashmap[prev] > hashmap[current]:
                    return 0
                j += 1
            
            if j == len(cs) and j != len(s):
                return 0
            s = A[i]
              
        return 1


