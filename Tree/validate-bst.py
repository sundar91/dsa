class Solution:
    def isValidBST(self, node):
        return int(self.checkBST(node, float("-inf"), float("inf")))

    def checkBST(self, node, lower, upper):
        if node is None:
            return True

        return (
            lower < node.val < upper
            and self.checkBST(node.left, lower, node.val)
            and self.checkBST(node.right, node.val, upper)
        )


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution2:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        stack = []
        node = A
        prev = float('-Inf')

        # Inorder traversal and check prev value is smaller
        # BST property -> Inorder sequence is in increasing order
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()

                if prev >= node.val:
                    return 0
                prev = node.val
                node = node.right

        return 1
