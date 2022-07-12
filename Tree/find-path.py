# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findPath(self, A, B, D):
        if A is None:
            return (D, False)

        D.append(A.val)
        if A.val == B:
            # copy data
            return (D, True)

        leftPath = self.findPath(A.left, B, D)
        if leftPath[1]:
            return leftPath

        righPath = self.findPath(A.right, B, D)
        if righPath[1]:
            return righPath

        D.pop()
        return (D, False)


root = TreeNode(15)
l1 = TreeNode(20)
l1.right = TreeNode(5)
l2 = TreeNode(35)
l1.left = l2
l2.left = TreeNode(8)

r1 = TreeNode(34)
r1.right = TreeNode(14)
r1.left = TreeNode(16)

root.left = l1
root.right = r1

print(Solution().findPath(root, 27, []))
