class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        s = A
        j = len(s)
        l = j
        j = j - 1
        count = 0
        i = 0
        ans = ""
        sr = ""
        for x in s:
            sr = x + sr

        # if string is already a palindrome, for even we need to change two characters
        if s == sr:
            if l % 2 == 1:
                ans = "YES"
            else:
                ans = "NO"
        else:
            while i <= j:
                if s[i] != s[j]:
                    count += 1
                i += 1
                j -= 1
            if count > 1:
                ans = "NO"
            else:
                ans = "YES"

        return ans
