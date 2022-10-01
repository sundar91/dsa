# There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

# We need to find bridges with minimal cost such that all islands are connected.

# It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.

from collections import defaultdict
import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        g = defaultdict(list)
        visited = {}

        for start, end, weight in B:
            g[start].append((weight, end))
            g[end].append((weight, start))

        q = []

        heapq.heappush(q, (0, 1))
        ans = 0
        while len(q) > 0:
            dist, v = heapq.heappop(q)

            if v in visited:
                continue

            ans += dist
            visited[v] = True

            for w, u in g[v]:
                if u not in visited:
                    heapq.heappush(q, (w, u))

        return ans


print(Solution().solve(4, [
    [1, 2, 1],
    [2, 3, 2],
    [3, 4, 4],
    [1, 4, 3]
]))
