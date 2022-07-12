# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


h = {}


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree

    def buildTree(self, A, B):
        global h
        n = len(A)
        for i in range(n):
            h[A[i]] = i

        return self.build(A, B, n-1, 0, 0, n-1)

    def build(self, A, B, ps, pe, ist, ie):
        if ps < pe:
            return None

        val = B[ps]
        node = TreeNode(val)
        indx = h[val]

        node.left = self.build(A, B, ps - ie + indx - 1, pe, ist, indx - 1)
        node.right = self.build(A, B, ps-1, ps-ie + indx, indx + 1, ie)

        return node


print(Solution().buildTree([1], [1]))
