# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return True

        if A is None or B is None:
            return False

        if A.val != B.val:
            return False

        return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)
