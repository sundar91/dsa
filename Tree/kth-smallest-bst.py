# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    # Moris inorder traversal (Inorder traversal in bst is always sorted)
    def kthsmallest(self, A, B):
        res = -1
        count = 0
        while A:
            if A.left is None:
                res = A.val
                count += 1
                A = A.right

            else:
                temp = A.left
                while temp.right and temp.right != A:
                    temp = temp.right

                if temp.right is None:
                    temp.right = A
                    A = A.left

                elif temp.right == A:
                    temp.right = None
                    res = A.val
                    count += 1
                    A = A.right
            if count == B:
                break
        return res
