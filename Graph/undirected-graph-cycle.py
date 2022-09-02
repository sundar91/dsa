from collections import defaultdict


class Solution:

    def __init__(self):
        self.visited = []
        self.iscycle = False

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def solve(self, A, B):

        self.visited = [False] * (A+1)
        self.iscycle = False

        adj = defaultdict(list)

        for i in range(len(B)):
            adj[B[i][0]].append(B[i][1])
            adj[B[i][1]].append(B[i][0])

        print(adj)

        for i in range(1, A + 1):
            if self.visited[i] == False:
                self.dfs(adj, i, 0)

        return int(self.iscycle)

    def dfs(self, adj, v, prev):
        self.visited[v] = True

        for u in adj[v]:
            if u != prev:
                if self.visited[u] == False:
                    self.dfs(adj, u, v)
                else:
                    self.iscycle = True


print(Solution().solve(5, [[1, 2], [1, 3], [2, 3], [1, 4], [4, 5]]))
