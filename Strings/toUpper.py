# You are given a function to_upper() consisting of a character array A.

# Convert each charater of A into Uppercase character if it exists. 
# If the Uppercase of a character does not exist, it remains unmodified.
# The lowercase letters from a to z is converted to uppercase letters 
# from A to Z respectively.

# Return the uppercase version of the given character array.

class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        for i in range(len(A)):
            if ord(A[i]) >= 97 and ord(A[i]) < 123:
                A[i] = chr(ord(A[i]) -32)
        return A; 
