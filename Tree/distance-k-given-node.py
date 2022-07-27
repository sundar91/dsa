# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    def solve(self, A, B):
        return self.findKDistanceDown(A, B)

    def findKDistanceDown(self, node, k):
        if node is None or k < 0:
            return

        if k == 0:
            print(node.val)
            return

        self.findKDistanceDown(node.left, k - 1)
        self.findKDistanceDown(node.right, k - 1)

    def findKDistanceNode(self, root, target, k):
        if root is None:
            return -1

        if root == target:
            self.findKDistanceDown(root, k)
            return 0

        dl = self.findKDistanceNode(root.left, target, k)
        # if target found in left subtree
        if dl != -1:

            if dl + 1 == k:
                print(root.val)
            else:
                self.findKDistanceDown(root.right, target, dl - k - 2)

            return 1 + dl

        # if target not found on left search right
        dr = self.findKDistanceNode(root.right, target, k)
        if dr != -1:

            if dr + 1 == k:
                print(root.val)
            else:
                # why -2? Becase left is 2 distance away from right node
                self.findKDistanceDown(root.left, dr - k - 2)

            return 1 + dr

        return -1
