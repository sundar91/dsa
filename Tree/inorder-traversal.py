class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, A):
        stack = []
        res = []
        node = A
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right

        return res


root = TreeNode(1)
r = TreeNode(2)
r.left = TreeNode(3)
root.right = r

print(Solution().inorderTraversal(root))
