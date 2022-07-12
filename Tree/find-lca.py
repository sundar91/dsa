# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):

        # find path of B node
        pathB = self.findPath(A, B, [])[0]

        # find path of C node
        pathC = self.findPath(A, C, [])[0]

        n = min(len(pathB), len(pathC))

        lca = -1
        for i in range(n):
            if pathB[i] == pathC[i]:
                lca = pathB[i]
                continue

            break

        return lca

    def findPath(self, A, B, D):
        if A is None:
            return (D, False)

        D.append(A.val)

        if A.val == B:
            return (D, True)

        leftPath = self.findPath(A.left, B, D)
        if leftPath[1]:
            return leftPath

        righPath = self.findPath(A.right, B, D)
        if righPath[1]:
            return righPath

        D.pop()
        return (D, False)
