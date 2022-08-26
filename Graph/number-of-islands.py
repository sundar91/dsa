import sys
sys.setrecursionlimit(100000)


class Solution:
    def __init__(self):
        self.visited = {}

    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        self.visited = {}
        n = len(A)
        m = len(A[0])
        count = 0
        for i in range(n):
            for j in range(m):

                if (i, j) not in self.visited and A[i][j] == 1:
                    self.dfs(A, i, j)
                    count += 1

        return count

    def dfs(self, A, i, j):

        n = len(A)
        m = len(A[0])

        adj = [(i-1, j), (i, j-1), (i+1, j), (i, j + 1), (i-1, j-1),
               (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1)]

        self.visited[(i, j)] = True
        for node in adj:
            x, y = node[0], node[1]
            if x >= 0 and x < n and y >= 0 and y < m and (x, y) not in self.visited and A[x][y] == 1:
                self.dfs(A, x, y)


print(Solution().solve([
    [0, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 1]
]))
