class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        n = len(A[0])

        dp = [0] * (n)
        dp[0] = max(A[0][0], A[1][0])

        if n < 2:
            return dp[0]

        dp[1] = max(A[0][1], A[1][1])
        dp[1] = max(dp[0], dp[1])

        for i in range(2, n):
            mc = max(A[0][i], A[1][i])
            dp[i] = max(dp[i-1], mc + dp[i-2])

        print(dp)
        return dp[n-1]


class Solution2:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, V):
        assert(len(V) == 2 and len(V) <= 20000)
        N = len(V[0])

        MAXSUM = [[0, 0] for i in range(N+1)]

        ele = max(V[0][0], V[1][0])
        MAXSUM[0][1] = ele
        for i in range(1, N):

            # take the maximum of both the element in the current column.
            cur_element = max(V[0][i], V[1][i])

            # Case 1: Do not include current element.
            MAXSUM[i][0] = max(MAXSUM[i-1][0], MAXSUM[i-1][1])

            # Case 2: Include current element
            MAXSUM[i][1] = cur_element + MAXSUM[i-1][0]

        return max(MAXSUM[N-1][0], MAXSUM[N-1][1])


print(Solution().adjacent([
    [16, 5, 54, 55, 36, 82, 61, 77, 66, 61],
    [31, 30, 36, 70, 9, 37, 1, 11, 68, 14]
]))
