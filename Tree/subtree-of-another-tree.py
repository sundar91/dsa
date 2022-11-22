# Given the roots of two binary trees root and subRoot, return true
# if there is a subtree of root with the same structure and node values of subRoot
# and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Exmaple:
# Input: root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
# Output: true


class Solution:
    def isSubtree(self, root, subRoot) -> bool:

        def isSameTree(p, q):
            if p is None and q is None:
                return True

            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        if subRoot is None:
            return True

        if root is None:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
