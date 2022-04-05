# You are given a string A of size N consisting of lowercase alphabets.

# You can change at most B characters in the given string to any other lowercase alphabet such that 
# the number of distinct characters in the string is minimized.

# Find the minimum number of distinct characters in the resulting string.

# A = "abcabbccd"
# B = 3
# output - > 2

# We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
# So the minimum number of distinct character will be 2.

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arr = [0] * 26
        res = 0
        for i in range(len(A)):
            arr[ord(A[i]) - ord('a')] += 1 
            if arr[ord(A[i]) - ord('a')] == 1:
                res += 1
        
        arr.sort()

        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            
            if arr[i] > B:
                break
            
            res -= 1
            B = B - arr[i]
        
        return res