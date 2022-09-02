from collections import defaultdict, deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        g = defaultdict(list)
        for start, end in B:
            g[start].append(end)
            g[end].append(start)
        visited = {}
        for i in range(A):
            if i not in visited:
                color = 1
                q = deque()
                q.append(i)
                visited[i] = 0
                while q:
                    sz = len(q)
                    for _ in range(sz):
                        top = q.popleft()
                        if top in g:
                            for neigh in g[top]:
                                if neigh in visited:
                                    if visited[neigh] == 1-color:
                                        return 0
                                else:
                                    visited[neigh] = color
                                    q.append(neigh)
                    color = 1 - color
        return 1
