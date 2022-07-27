# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if A is None:
            return 0
        if A.val == B and A.left is None and A.right is None:
            return 1
        return self.hasPathSum(A.left, B - A.val) or self.hasPathSum(A.right, B - A.val)
