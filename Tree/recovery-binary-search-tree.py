# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        node = A
        prev = float('-inf')
        res = [-1, -1]
        isFirst = True
        while node:
            # find two wrong node
            if prev >= node.val:
                if res[0] == -1:
                    res[0] = prev
                    res[1] = node.val
                else:
                    isFirst = False
                    res[1] = node.val

            if node.left is None:
                # change previous until we reach second inversion, once we find 2 inversion we don't need to maintain prev
                if prev < node.val and isFirst:
                    prev = node.val
                node = node.right
            else:
                temp = node.left

                while temp.right is not None and temp.right != node:
                    temp = temp.right

                if temp.right is None:
                    temp.right = node
                    node = node.left
                elif temp.right == node:
                    temp.right = None
                    # change previous until we reach second inversion, once we find 2 inversion we don't need to maintain prev
                    if prev < node.val and isFirst:
                        prev = node.val
                    node = node.right

        return sorted(res)


root = TreeNode(2)
l1 = TreeNode(3)

r1 = TreeNode(1)
r2 = TreeNode(4)
r1.right = r2
r2.right = TreeNode(5)

root.left = l1
root.right = r1

print(Solution().recoverTree(root))
