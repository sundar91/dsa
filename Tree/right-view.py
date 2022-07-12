# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

from collections import deque


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        q = deque()
        q.append(A)
        res = []
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)

        return res
