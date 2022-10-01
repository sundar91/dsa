import heapq


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        maxQ, minQ = [], []

        heapq.heappush(maxQ, -A[0])
        median = -1 * maxQ[0]
        n = len(A)
        for i in range(1, n):
            if median == A[i]:
                return 1

            if A[i] < median:
                heapq.heappush(maxQ, -A[i])
            else:
                heapq.heappush(minQ, A[i])

            if (len(maxQ) - len(minQ)) > 1:
                m = heapq.heappop(maxQ)
                heapq.heappush(minQ, -m)
            elif (len(minQ) - len(maxQ)) >= 1:
                m = heapq.heappop(minQ)
                heapq.heappush(maxQ, -m)

            if len(maxQ) == len(minQ):
                median = (-1 * maxQ[0] + minQ[0]) / 2
            else:
                median = -1 * maxQ[0]

        maxQ, minQ = [], []
        heapq.heappush(maxQ, -A[n-1])
        median = -1 * maxQ[0]
        for i in range(n-2, -1, -1):
            if median == A[i]:
                return 1

            if A[i] < median:
                heapq.heappush(maxQ, -A[i])
            else:
                heapq.heappush(minQ, A[i])

            if (len(maxQ) - len(minQ)) > 1:
                m = heapq.heappop(maxQ)
                heapq.heappush(minQ, -m)
            elif (len(minQ) - len(maxQ)) >= 1:
                m = heapq.heappop(minQ)
                heapq.heappush(maxQ, -m)

            if len(maxQ) == len(minQ):
                median = (-1 * maxQ[0] + minQ[0]) / 2
            else:
                median = -1 * maxQ[0]

        return 0


print(Solution().solve([2, 7, 3, 1]))
