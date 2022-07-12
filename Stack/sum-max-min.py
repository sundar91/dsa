from collections import deque


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        minQ = deque()
        maxQ = deque()
        mod = pow(10, 9) + 7
        s = 0

        for i in range(n):

            while len(minQ) > 0 and A[minQ[-1]] >= A[i]:
                minQ.pop()

            if len(minQ) > 0 and minQ[0] <= i - B:
                minQ.popleft()

            while len(maxQ) > 0 and A[maxQ[-1]] <= A[i]:
                maxQ.pop()

            if len(maxQ) > 0 and maxQ[0] <= i - B:
                maxQ.popleft()

            minQ.append(i)
            maxQ.append(i)

            if i >= B - 1:
                s += A[minQ[0]] + A[maxQ[0]]
                s = s % mod

        return s


print(Solution().solve([2, 5, -1, 7, -3, -1, -2], 4))
