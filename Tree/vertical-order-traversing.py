# Definition for a  binary tree node
from collections import deque
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class DepthInfo:
    def __init__(self, node, d):
        self.node = node
        self.dis = d


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        maxDepth, minDepth = float('-Inf'), float('Inf')
        h = defaultdict(lambda: [])
        q = deque()
        res = []

        q.append(DepthInfo(A, 0))
        while q:
            info = q.popleft()

            h[info.dis].append(info.node.val)
            maxDepth = max(maxDepth, info.dis)
            minDepth = min(minDepth, info.dis)

            if info.node.left:
                q.append(DepthInfo(info.node.left, info.dis - 1))

            if info.node.right:
                q.append(DepthInfo(info.node.right, info.dis + 1))

        for i in range(minDepth, maxDepth + 1):
            res.append(h[i])

        return res
