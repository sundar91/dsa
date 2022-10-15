from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        ans = float('-inf')

        g = defaultdict(list)
        for i in range(1, len(A)):
            g[A[i]].append(i)
            g[i].append(A[i])

        visited = {}

        def dfs(node):

            nonlocal ans
            visited[node] = True

            o = 1
            max1, max2 = 0, 0

            for i in g[node]:
                if i in visited:
                    continue

                current = dfs(i)

                if current >= max1:
                    max2 = max1
                    max1 = current

                elif current >= max2:
                    max2 = current

                o = max(o, current + 1)

            ans = max(ans, max1 + max2)
            return o

        dfs(0)
        return ans


print(Solution().solve([-1, 0, 0]))
