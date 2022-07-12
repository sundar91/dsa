# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        info = self.checkBST(A)
        return info[0]

    def checkBST(self, A):
        if A is None:
            return (0, True)

        left = self.checkBST(A.left)
        right = self.checkBST(A.right)

        lower, upper = float('-Inf'), float('Inf')

        if A.left:
            lower = A.left.val

        if A.right:
            upper = A.right.val

        isBST = left[1] and right[1]
        if isBST:
            if A.val > lower and A.val < upper:
                return (1 + left[0] + right[0], True)

        return (max(left[0], right[0]), False)


root = TreeNode(9)
root.left = TreeNode(10)
r = TreeNode(6)
r.left = TreeNode(3)
root.right = r

print(Solution().solve(root))
