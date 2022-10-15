class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @param G : list of integers
    # @param H : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F, G, H):

        g = [[float('inf') for _ in range(A + 1)] for _ in range(A + 1)]

        for i in range(B):
            g[D[i]][E[i]] = min(F[i], g[D[i]][E[i]])
            g[E[i]][D[i]] = min(F[i],  g[E[i]][D[i]])

        for k in range(A + 1):
            for i in range(A + 1):
                for j in range(A + 1):
                    if i == j:
                        g[i][j] = 0
                    else:
                        g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        res = []
        for i in range(C):
            r = g[G[i]][H[i]]
            res.append(-1 if r == float('inf') else r)

        return res
