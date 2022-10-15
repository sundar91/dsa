from collections import defaultdict


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):

        g = defaultdict(list)
        n = len(A)

        indeg = defaultdict(lambda: 0)
        outdeg = defaultdict(lambda: 0)

        for i in range(n):
            st = A[i]

            s = st[0]
            e = st[-1]

            indeg[e] = 1 + indeg.get(e, 0)
            outdeg[s] = 1 + outdeg.get(s, 0)
            g[s].append(e)

        for i in range(26):
            alpha = chr(i + ord('a'))
            if indeg[alpha] != outdeg[alpha]:
                return 0

        visited = {}

        def dfs(visited, ind):

            visited[ind] = True
            for i in g[ind]:
                if i not in visited:
                    dfs(visited, i)

        dfs(visited, A[0][0])

        for i in range(26):
            alpha = chr(i + ord('a'))
            if len(g[alpha]) > 0 and alpha not in visited:
                return 0

        return 1


input = ["aab", "bac", "aaa", "cd"]
print(Solution().solve(input))
