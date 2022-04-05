# Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
# The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
# Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

class Solution:
    # @param A : list of strings
    # @return a string
    def longestCommonPrefix(self, A):
        n = len(A)
        if n < 1:
            return ""
        prefix = A[0]
        prefixLen = len(prefix)
        for i in range(1, n):
            j = 0
            while j < min(prefixLen, len(A[i])):
                if prefix[j] != A[i][j]:
                    break
                j += 1
            if j < prefixLen:
                prefix = prefix[:j]
                prefixLen = j
        return prefix