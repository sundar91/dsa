# You are given a function to_lower() which takes a character array A as an argument.

# Convert each character of A into lowercase character if it exists. 
# If the lowercase of a character does not exist, it remains unmodified.
# The uppercase letters from A to Z is converted to lowercase letters from a to z respectively.

# Return the lowercase version of the given character array.

class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        for i in range(len(A)):
            if ord(A[i]) >= 65 and ord(A[i]) < 91:
                A[i] = chr(ord(A[i]) + 32)
        return A