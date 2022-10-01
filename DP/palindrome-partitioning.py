class Solution:
    def isPalindrome(self, A):
        dp = []
        n = len(A)
        for i in range(n):
            dp.append([True] * n)
        for l in range(2, n+1):  # considering window size from 2 to n(inclusive)
            # last index of start will be n-l (inclusive)
            for start in range(n - l + 1):
                end = start + l - 1
                dp[start][end] = A[start] == A[end] and dp[start + 1][end - 1]
        return dp

    # @param A : string
    # @return an integer
    def minCut(self, A):
        n = len(A)
        isPalindrome = self.isPalindrome(A)
        dp = [-1 for i in range(n)]
        dp[0] = 0
        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0
            else:
                mini = float('inf')
                for j in range(i, 0, -1):
                    if isPalindrome[j][i]:  # get the min cut for all the substrings before i
                        if dp[j - 1] < mini:
                            mini = dp[j - 1]
                dp[i] = mini + 1
        return dp[n - 1]
