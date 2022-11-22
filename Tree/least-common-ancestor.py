# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self) -> None:
        self.lca = []

    def lowestCommonAncestor(self, root, p, q):
        st = []

        def dfs(node: TreeNode):

            if node is None:
                return
            if node.val == p:
                self.lca = st.copy()
                return

            st.append(node.val)
            dfs(node.left)
            dfs(node.right)
            st.pop()

        dfs(root)
        print(self.lca)


root = TreeNode(6)
l = TreeNode(2)
root.left = l
r = TreeNode(8)
l.left = TreeNode(0)
l.right = TreeNode(4)
root.right = r

print(Solution().lowestCommonAncestor(root, 4, 8))
