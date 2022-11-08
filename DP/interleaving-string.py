# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

# Example:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [[False for _ in range(m+1)] for _ in range(n+1)]

        dp[n][m] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and s3[i+j] == s1[i] and dp[i + 1][j]:
                    dp[i][j] = True

                if j < m and s3[i+j] == s2[j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
