import heapq
from collections import defaultdict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HeapMap:
    def __init__(self):
        self.arr = []
        self.d = {}

    def heappush(self, key, val):
        node = Node(key, val)
        self.arr.append(node)
        i = len(self.arr) - 1
        self.d[key] = i
        self.move_node_up(i)

    def move_node_up(self, i):
        while i > 0:
            p = self.parent(i)
            if self.arr[i].val < self.arr[p].val:
                self.swap(i, p)
                i = p
            else:
                break

    def swap(self, i, p):
        keyi = self.arr[i].key
        keyp = self.arr[p].key
        self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
        self.d[keyi] = p
        self.d[keyp] = i

    def heappop(self):
        self.swap(0, len(self.arr) - 1)
        result = self.arr.pop()
        self.heapify(0)
        del self.d[result.key]
        return result.key, result.val

    def heapify(self, i):
        smaller = i
        left = self.left(i)
        right = self.right(i)
        if left < len(self.arr) and self.arr[left].val < self.arr[i].val:
            smaller = left
        if right < len(self.arr) and self.arr[right].val < self.arr[smaller].val:
            smaller = right
        if smaller != i:
            self.swap(smaller, i)
            self.heapify(smaller)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) / 2

    def decrease_key(self, key, new_val):
        # print self.arr, self.d, key, new_val
        if key not in self.d:
            self.heappush(key, new_val)
            return
        idx = self.d[key]
        if self.arr[idx].val > new_val:
            self.arr[idx].val = new_val
            self.move_node_up(idx)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, src):
        if A <= 0:
            return []
        dist = [float("inf") for _ in range(A)]
        g = defaultdict(list)

        for start, end, wgt in B:
            g[start].append((end, wgt))
            g[end].append((start, wgt))

        h = HeapMap()
        h.decrease_key(src, 0)
        visited = [False for _ in range(A)]

        while h.arr:
            key, val = h.heappop()
            dist[key] = val
            visited[key] = True

            if key in g:
                for neigh, dd in g[key]:
                    if not visited[neigh]:
                        h.decrease_key(neigh, val + dd)

        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist


# using in build heap
class Solution2:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        d = [-1] * (A)
        q = []
        g = defaultdict(list)

        for start, end, w in B:
            g[start].append((end, w))
            g[end].append((start, w))

        heapq.heappush(q, (0, C))

        while len(q) > 0:
            v = heapq.heappop(q)

            dist, node = v[0], v[1]
            if d[node] != -1:
                continue

            d[node] = dist

            for u in g[node]:
                if d[u[0]] == -1:
                    heapq.heappush(q, (dist + u[1], u[0]))

        return d
