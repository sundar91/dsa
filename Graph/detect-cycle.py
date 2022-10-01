from collections import defaultdict, deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        adj = defaultdict(list)

        indeg = defaultdict(lambda: 0)

        for s, e in B:
            adj[s].append(e)
            indeg[e] += 1

        q = deque()

        for i in range(1, A + 1):
            if indeg[i] == 0:
                q.append(i)

        ans = []
        while len(q) > 0:
            node = q.popleft()
            ans.append(node)
            for n in adj[node]:
                indeg[n] -= 1

                if indeg[n] == 0:
                    q.append(n)

        if len(ans) != A:
            return 1

        return 0


input = [[1, 2],
         [2, 3],
         [3, 4],
         [4, 5]]

print(Solution().solve(2, [[1, 2]]))
