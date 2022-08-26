from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def __init__(self):
        self.visited = {}

    def solve(self, A, B, C):

        self.visited = {}
        adj = defaultdict(list)
        for i in range(len(A)):
            adj[A[i]].append(i + 1)

        print(adj)
        return int(self.dfs(adj, C, B))

    def dfs(self, adj, f, t):

        self.visited[f] = True

        for a in adj[f]:
            if a == t:
                return True

            if a not in self.visited:
                if self.dfs(adj, a, t):
                    return True

        return False


print(Solution().solve([1, 1, 2, 3, 4, 3, 4, 1], 7, 7))
