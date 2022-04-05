# Given an integer array A of size N, find the first repeating element in it.

# We need to find the element that occurs more than once and whose index of first occurrence is smallest.

# If there is no repeating element, return -1.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # Initialize index of first repeating element
        mini = -1
    
        # Creates an empty hashset named ump
        ump = {}
    
        # Traverse the input array from right to left
        for i in range(n-1, -1, -1):
            # If element is already in hash set, update min
            if (ump.get(A[i]) != None):
                mini = i
            else:   # Else add element to hash set
                ump[A[i]] = 1
        
        if(mini == -1):
            return mini
        
        return A[mini]