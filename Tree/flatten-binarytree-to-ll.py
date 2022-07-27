# Definition for a  binary tree node
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        store = current = A
        while current:
            if current.left:
                prev = current.left
                while prev.right:
                    prev = prev.right
                prev.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
        return store


root = TreeNode(1)
l1 = TreeNode(2)
# l1.right = TreeNode(5)
# l2 = TreeNode(35)
# l1.left = l2
# l2.left = TreeNode(8)

r1 = TreeNode(3)
rl = TreeNode(4)
rl.right = TreeNode(5)
r1.left = rl

root.left = l1
root.right = r1

print(Solution().flatten(root))
