import heapq


class Node:
    def __init__(self, cur_val, org_val):
        self.cur_val = cur_val
        self.org_val = org_val

    def __lt__(self, other):
        return (self.cur_val + self.org_val) < (other.cur_val + other.org_val)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        h = []

        maxelement = A[0]
        for i in range(n):
            heapq.heappush(h, Node(A[i], A[i]))
            maxelement = max(maxelement, A[i])

        if B < n:
            return maxelement

        for _ in range(B):
            node = heapq.heappop(h)
            c = node.cur_val + node.org_val
            heapq.heappush(h, Node(c, node.org_val))
            maxelement = max(maxelement, c)
        return maxelement


print(Solution().solve([8, 6, 4, 2], 8))
