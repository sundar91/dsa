# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return int(self.compare(A.left, A.right))

    def compare(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        return self.compare(node1.left, node2.right) and self.compare(node1.right, node2.left)
