# Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
# You may assume that the array is non-empty and the majority element always exists in the array.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        count = 1
        me = A[0]
        for i in range(1, len(A)):
            if me == A[i]:
                count += 1
            elif count == 0:
                me = A[i]
                count = 1
            else:
                count -= 1
        
        freq = 0
        for i in range(len(A)):
            if me == A[i]:
                freq += 1
        
        if freq > (len(A)/ 2):
            return me
        
        return -1