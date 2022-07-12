from collections import deque, defaultdict
# Definition for a  binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        h = defaultdict(lambda: [])
        res = []
        q = deque()

        q.append([A, 0])
        max_depth, min_depth = float('-inf'), float('inf')

        while q:
            info = q.popleft()

            h[info[1]].append(info[0].val)
            max_depth = max(max_depth, info[1])
            min_depth = min(min_depth, info[1])

            if info[0].left:
                q.append([info[0].left, info[1] - 1])

            if info[0].right:
                q.append([info[0].right, info[1] + 1])

        for i in range(min_depth, max_depth + 1):
            res.append(h[i][0])

        return res
