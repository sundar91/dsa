# Definition for a  binary tree node
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A:
            return 0
        if A.val < B:
            return self.solve(A.right, B, C)
        if A.val > C:
            return self.solve(A.left, B, C)
        return 1 + self.solve(A.left, B, C) + self.solve(A.right, B, C)


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        q = deque()
        cnt = 0
        q.append(A)
        while q:
            node = q.popleft()
            if node.val <= B:
                # go right
                if node.right:
                    q.append(node.right)

            elif node.val >= C:
                # go left
                if node.left:
                    q.append(node.left)

            else:
                # go both side
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if B <= node.val <= C:
                cnt += 1

        return cnt


root = TreeNode(15)
l1 = TreeNode(12)
l1.right = TreeNode(14)
l2 = TreeNode(10)
l1.left = l2
l2.left = TreeNode(8)

r1 = TreeNode(20)
r1.right = TreeNode(27)
r1.left = TreeNode(16)

root.left = l1
root.right = r1

print(Solution().solve(root, 12, 20))
