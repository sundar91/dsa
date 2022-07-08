# Definition for a  binary tree node
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):

        root = TreeNode(A[0])
        temp = root
        q = deque()
        q.append(temp)
        i = 1
        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node is None:
                    continue

                if A[i] != -1:
                    left = TreeNode(A[i])
                    node.left = left
                    q.append(node.left)
                else:
                    q.append(None)

                i += 1

                if A[i] != -1:
                    right = TreeNode(A[i])
                    node.right = right
                    q.append(node.right)
                else:
                    q.append(None)

                i += 1

        return root


print(Solution().solve([1, 2, 3, 4, 5, -1, -1, -1, -1, -1, 6, -1, -1]))
