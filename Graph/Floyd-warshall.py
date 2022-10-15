import math


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        dist = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                if A[i][j] == -1:
                    temp.append(math.inf)
                else:

                    temp.append(A[i][j])
            dist.append(temp)

        vertices = len(A)
        for k in range(vertices):
            for i in range(vertices):
                for j in range(vertices):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

        for i in range(len(dist)):
            for j in range(len(dist[0])):
                if dist[i][j] == math.inf:
                    dist[i][j] = -1

        return dist
