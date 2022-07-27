# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if B > C:
            B, C = C, B
        self.distanceBetween(A, B, C)

    def distanceBetween(self, node, a, b):
        if node is None:
            return 0

        if node.val > a and node.val > b:
            return self.distanceBetween(node.left, a, b)

        if node.val < a and node.val < b:
            return self.distanceBetween(node.right, a, b)

        if node.val >= a and node.val <= b:
            return self.distanceFromNode(node, a) + self.distanceFromNode(node, b)

    def distanceFromNode(self, node, a):
        if node.val == a:
            return 0

        if node.val >= a:
            return 1 + self.distanceFromNode(node.left, a)

        return 1 + self.distanceFromNode(node.right, a)
