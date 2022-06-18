# Given a string A of size N, find and return the longest palindromic substring in A.

# Substring of string A is A[i...j] where 0 <= i <= j < len(A)

# Palindrome string:
# A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

# Incase of conflict, return the substring which occurs first ( with the least starting index).

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        ans = 0
        start = 0
        end = 0

        for i in range(len(A)):
            x, y = self.expand(A, i, i)
            if y - x - 1 > ans:
                start = x
                end = y
                ans = end - start - 1

        for i in range(len(A)-1):
            x, y = self.expand(A, i, i+1)
            if y - x - 1 > ans:
                start = x
                end = y
                ans = end - start - 1
        # return start, end, ans
        return A[start+1:end]

    def expand(self, A, p1, p2):
        while p1 >= 0 and p2 < len(A) and A[p1] == A[p2]:
            p1 -= 1
            p2 += 1
        # p2-p1-1
        return (p1, p2)
