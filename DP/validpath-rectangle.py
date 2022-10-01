from collections import deque
import math
import sys


sys.setrecursionlimit(1000000)


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):

        x, y = A, B
        rect = [[0 for _ in range(y + 1)] for _ in range(x + 1)]

        posx = [-1, -1, -1, 0, 0, 1, 1, 1]
        posy = [0, 1, -1, -1, 1, -1, 0, 1]
        visited = set()
        ans = "NO"

        def isValid(nx, ny):
            if nx >= 0 and nx <= x and ny >= 0 and ny <= y:
                return True
            return False

        def dfs(row, col):
            nonlocal ans
            nonlocal visited
            if row == x and col == y:
                ans = "YES"
                return

            visited.add((row, col))

            for k in range(8):
                newx = posx[k] + row
                newy = posy[k] + col
                if isValid(newx, newy) and (newx, newy) not in visited and rect[row][col] != 1:
                    dfs(newx, newy)

        for i in range(x + 1):
            for j in range(y + 1):
                for k in range(C):
                    d = math.pow(i - E[k], 2) + math.pow(j - F[k], 2)
                    if d <= (D * D):
                        rect[i][j] = 1

        if rect[x][y] == 1 or rect[0][0] == 1:
            return 'NO'

        dfs(0, 0)

        return ans
