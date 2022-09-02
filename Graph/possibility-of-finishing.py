from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):

        adj = defaultdict(list)

        indeg = [0] * (A + 1)

        for i in range(len(B)):
            adj[B[i]].append(C[i])
            indeg[C[i]] += 1

        res = []
        q = []

        for i in range(1, A+1):
            if indeg[i] == 0:
                q.append(i)

        while len(q) > 0:
            v = q.pop(0)

            for u in adj[v]:
                indeg[u] -= 1
                if indeg[u] == 0:
                    q.append(u)

        if len(res) == A:
            return 1

        return 0


b = [1, 3, 4, 5]
c = [2, 1, 5, 3]

print(Solution().solve(5, b, c))
