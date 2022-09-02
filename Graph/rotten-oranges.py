class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        n, m = len(A), len(A[0])
        q = []
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = {}
        fo = 0

        for i in range(n):
            for j in range(m):
                if A[i][j] == 2:
                    q.append((i, j))
                    visited[(i, j)] = True
                elif A[i][j] == 1:
                    fo += 1

        res = 0

        while len(q) > 0:
            s = len(q)
            flag = False
            for _ in range(s):
                i, j = q.pop(0)
                for k in range(4):
                    newI = i + dx[k]
                    newJ = j + dy[k]

                    if newI >= 0 and newI < n and newJ >= 0 and newJ < m and A[newI][newJ] == 1 and (newI, newJ) not in visited:
                        flag = True
                        q.append((newI, newJ))
                        visited[(newI, newJ)] = True
                        A[newI][newJ] = 2
                        fo -= 1

            if flag:
                res += 1

        if fo > 0:
            return -1

        return res


A1 = [[2, 1, 1],
      [1, 1, 0],
      [0, 1, 1]]

A2 = [
    [2, 0, 2, 2, 2, 0, 2, 1, 1, 0],
    [0, 1, 2, 0, 2, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 2, 0, 1, 1, 2, 1],
    [2, 0, 2, 0, 1, 1, 2, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 2, 0, 2, 2],
    [0, 2, 1, 1, 2, 2, 0, 2, 1, 2],
    [2, 1, 0, 2, 0, 0, 0, 0, 1, 1],
    [2, 2, 0, 2, 2, 1, 1, 1, 2, 2]
]

print(Solution().solve(A1))
