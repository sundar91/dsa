class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        count = 0
        for i in range(n):

            l, r = i, i
            while l >= 0 and r < n and s[i] == s[r]:
                l -= 1
                r += 1
                count += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[i] == s[r]:
                l -= 1
                r += 1
                count += 1

        return count


print(Solution().countSubstrings("aba"))
