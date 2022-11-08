
# Two pointers
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res = ""
        resLen = 0
        for i in range(n):

            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - l - 1 > resLen:
                resLen = r - l - 1
                res = s[l + 1: r]

            l, r = i, i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - l - 1 > resLen:
                resLen = r - l - 1
                res = s[l + 1: r]

        return res


print(Solution().longestPalindrome("babad"))
