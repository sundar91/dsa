# Definition for a  binary tree node
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        q = deque()

        q.append(A)
        sumEven, sumOdd = 0, 0

        isOdd = True

        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                node = q.popleft()
                s += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if isOdd:
                sumOdd += s
            else:
                sumEven += s

            isOdd = not isOdd

        return sumOdd - sumEven
