class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        wordHash = set()
        for word in wordDict:
            wordHash.add(word)

        n = len(s)
        dp = [False] * n
        h = []

        for i in range(n):
            w = s[:i+1]
            if w in wordHash:
                dp[i] = True
                h.append(i)

            l = len(h)
            for j in range(l):
                w = s[(h[j] + 1):i+1]
                if w in wordHash:
                    dp[i] = True
                    h.append(i)

        return dp[n-1]


class Solution2:
    def wordBreak(self, s: str, wordDict) -> bool:

        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                #check each word if it
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]


print(Solution().wordBreak('catsanddog', [
      "cats", "dog", "sand", "and", "cat"]))
