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
    def zigzagLevelOrder(self, A):
        q = deque()
        q.append(A)
        res = []
        isOdd = True

        while q:
            n = len(q)
            arr = []
            for _ in range(n):
                if isOdd:
                    node = q.pop()
                    arr.append(node.val)
                    if node.left:
                        q.appendleft(node.left)

                    if node.right:
                        q.appendleft(node.right)

                else:
                    node = q.popleft()
                    arr.append(node.val)
                    if node.right:
                        q.append(node.right)

                    if node.left:
                        q.append(node.left)

            res.append(arr)
            isOdd = not isOdd

        return res
