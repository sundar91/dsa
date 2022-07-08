# Definition for a  binary tree node
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        current_level = deque([A])
        next_level = deque()
        levels = [[A.val]]
        while current_level:
            node = current_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not current_level:
                if next_level:
                    levels.append([n.val for n in next_level])
                current_level = next_level
                next_level = deque()
        return levels


class Solution2:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        res = []
        q = deque()
        q.append(A)
        while len(q) > 0:
            n = len(q)
            arr = []
            for i in range(n):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

                arr.append(node.val)

            res.append(arr)

        return res
