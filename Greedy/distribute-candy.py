class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        candies = [1] * n

        # check from left
        for i in range(1, n):
            if A[i] > A[i-1]:
                candies[i] = candies[i-1] + 1

        # check from right and set max of left and right
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])

        s = 0
        for c in candies:
            s += c

        return s


a1 = [1, 5, 2, 1]
print(Solution().candy(a1))
