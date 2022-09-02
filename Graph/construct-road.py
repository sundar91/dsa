# A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.

# Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.

# Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.

# NOTE: All cities can be visited from any city. [connected component]

import sys
sys.setrecursionlimit(10**5)

maxN = 1e5 + 5
col = [0] * 2
g = [[]]
mod = 1e9+7


def dfs(u, pnode, c):
    col[c] += 1
    for v in g[u]:
        if(v != pnode):
            dfs(v, u, 1-c)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        global col, g
        N = A
        col = [0] * 2
        g = [[]for i in range(N+1)]

        for i in range(len(B)):
            u = B[i][0]
            v = B[i][1]
            g[u].append(v)
            g[v].append(u)
        dfs(1, 0, 0)
        ans = col[0] * col[1]
        ans -= N-1
        return int(ans % mod)
