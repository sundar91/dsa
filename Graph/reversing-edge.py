from collections import deque, defaultdict
from heapq import heappush, heappop


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def reverseEdges(self, A, B):

        adj = defaultdict(list)
        revAdj = defaultdict(list)
        for i in range(len(B)):
            adj[B[i][0]].append(B[i][1])
            revAdj[B[i][1]].append(B[i][0])

        q = []
        heappush(q, (0, 1))
        visited = set()
        ans = float('inf')
        while len(q) > 0:
            dist, node = heappop(q)

            if node == A:
                ans = min(ans, dist)

            visited.add(node)

            for neighbour in adj[node]:
                if neighbour in visited:
                    continue

                heappush(q, (dist, neighbour))

            for neighbour in revAdj[node]:
                if neighbour in visited:
                    continue

                heappush(q, (dist + 1, neighbour))

        return -1 if ans == float('inf') else ans
