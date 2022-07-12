import sys
# Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.

# The diameter of a tree is the number of edges on the longest path between two nodes in the tree. (longest path can be in left subtree also)


sys.setrecursionlimit(1000000000)


def height(root, ans):
    if root == None:
        return -1

    left_height = height(root.left, ans)

    right_height = height(root.right, ans)
    ans[0] = max(ans[0], 2 + left_height + right_height)

    return 1 + max(left_height, right_height)


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        ans = [0]
        height(A, ans)
        return ans[0]
