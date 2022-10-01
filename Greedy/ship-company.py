# Problem Description
# The local ship renting service has a special rate plan:

# It is up to a passenger to choose a ship.
# If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
# The passengers buy tickets in turn, the first person in the queue goes first, then the second one, and so on up to A-th person.

# You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.


import heapq


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):

        minQ = []
        maxQ = []

        for i in range(B):
            heapq.heappush(maxQ, -C[i])
            heapq.heappush(minQ, C[i])

        max_profit, min_profit = 0, 0

        for _ in range(A):
            maxVal = heapq.heappop(maxQ)
            minVal = heapq.heappop(minQ)

            max_profit += abs(maxVal)
            min_profit += minVal

            heapq.heappush(maxQ, -(abs(maxVal) - 1))
            heapq.heappush(minQ, (minVal - 1) if (minVal - 1)
                           > 0 else float('inf'))

        return [-maxQ[0], minQ[0]]


print(Solution().solve(4, 3, [2, 1, 1]))
