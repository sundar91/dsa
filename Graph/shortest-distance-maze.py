from collections import deque


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):

        ans = float('inf')

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        q = deque()
        q.append((B[0], B[1], 0))

        n = len(A)
        m = len(A[0])

        distance = [[float('inf') for _ in range(m)] for _ in range(n)]

        while len(q) > 0:
            x, y, d = q.popleft()

            if distance[x][y] <= d:
                continue

            distance[x][y] = d
            for i in range(4):
                xx, yy, l = x, y, d
                # keep moving to same direction
                while xx >= 0 and xx < n and yy >= 0 and yy < m and A[xx][yy] == 0:
                    xx += dx[i]
                    yy += dy[i]
                    l += 1
                xx -= dx[i]
                yy -= dy[i]
                l -= 1
                q.append((xx, yy, l))

        return -1 if distance[C[0]][C[1]] == float('inf') else distance[C[0]][C[1]]
