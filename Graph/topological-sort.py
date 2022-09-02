from collections import defaultdict, deque
import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        g = defaultdict(list)
        indeg = [0] * (A+1)

        #e = sorted(B, key=lambda x: x[1], reverse=True)
        for start, end in B:
            g[start].append(end)

            indeg[end] += 1

        q = []

        for i in range(1, A+1):
            if indeg[i] == 0:
                heapq.heappush(q, i)

        res = []
        while len(q) > 0:
            v = heapq.heappop(q)
            res.append(v)

            for u in g[v]:
                indeg[u] -= 1
                if indeg[u] == 0:
                    heapq.heappush(q, u)

        if len(res) == A:
            return res

        return []


r = [
    [1, 4],
    [1, 2],
    [4, 2],
    [4, 3],
    [3, 2],
    [5, 2],
    [3, 5],
    [8, 2],
    [8, 6]
]

print(Solution().solve(8, r))
