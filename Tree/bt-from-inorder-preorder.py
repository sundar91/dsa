class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        root_value = preorder[0]
        root_index = inorder.index(root_value)
        left_nodes = inorder[:root_index]
        right_nodes = inorder[root_index+1:]
        m, n = len(left_nodes), len(right_nodes)

        root = TreeNode(root_value)
        root.left = self.buildTree(preorder[1: m+1], left_nodes)
        root.right = self.buildTree(preorder[m+1:], right_nodes)
        return root


h = {}


class Solution2:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        global h
        n = len(A)
        for i in range(n):
            h[B[i]] = i

        return self.build(A, B, 0, n-1, 0, n - 1)

    def build(self, A, B, ps, pe, ist, ie):
        if ps > pe:
            return None

        val = A[ps]
        node = TreeNode(val)

        indx = h[val]  # find indx of number in inorder

        # first indx count will be on left
        node.left = self.build(A, B, ps + 1, ps + indx - ist, ist, indx - 1)
        node.right = self.build(A, B, ps + indx - ist + 1, pe, indx + 1, ie)

        return node
