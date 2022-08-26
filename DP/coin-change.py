class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # order is important
    def coinchange(self, A, B):
        dp = [0] * (B + 1)
        mod = int(1e6+7)
        A.sort()
        dp[0] = 1
        for i in range(1, B + 1):
            j = 0
            while j < len(A) and A[j] <= i:
                s = i - A[j]
                dp[i] += dp[s]
                j += 1

        return dp[B]

    def coinchange2(self, A, B):

        n = len(A)
        A.sort()

        first = [0] * (B + 1)
        second = [0] * (B + 1)

        for i in range(n - 1, -1, -1):
            for x in range(B + 1):
                if x == 0:
                    second[x] = 1
                    continue
                s = 0
                if A[i] <= x:
                    s = second[x - A[i]]
                second[x] = s + first[x]
                first = second

        print(first)
        print(second)
        return second[B]


print(Solution().coinchange2([1, 2, 3], 4))
