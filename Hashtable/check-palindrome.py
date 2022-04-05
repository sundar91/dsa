# Given a string A consisting of lowercase characters.
# Check if characters of the given string can be rearranged to form a palindrome.
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        hashmap = {}
        n = len(A)
        is_even = False
        if n % 2 == 0: 
            is_even = True

        for i in range(len(A)):
            if A[i] in hashmap:
                hashmap[A[i]] += 1
            else:
                hashmap[A[i]] = 1

        odd_count = 0
      
        for i in hashmap:
            if hashmap[i] % 2 != 0:
                odd_count += 1

        if odd_count > 1:
            return 0
        
        return 1