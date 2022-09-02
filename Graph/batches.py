from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        visited = {}
        g = defaultdict(list)
        count = 0

        for start, end in C:
            g[start].append(end)
            g[end].append(start)

        s = 0

        def dfs(v):
            nonlocal s
            visited[v] = True
            s += B[v-1]

            for u in g[v]:
                if u not in visited:
                    dfs(u)

        for i in range(1, A+1):
            if i not in visited:
                s = 0
                dfs(i)
                if s >= D:
                    count += 1

        return count


S = [2, 3, 10, 8, 4]
E = [
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 3],
    [4, 5]
]

print(Solution().solve(5, S, E, 34))
