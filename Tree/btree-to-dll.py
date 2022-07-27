import sys
sys.setrecursionlimit(10**5)

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# left is prev and right is next


def concatenate(leftList, rightList):
    if (leftList == None):
        return rightList
    if (rightList == None):
        return leftList

    leftLast = leftList.left

    rightLast = rightList.left
    if(leftLast != None):
        leftLast.right = rightList
    rightList.left = leftLast
    leftList.left = rightLast
    if(rightLast != None):
        rightLast.right = leftList
    return leftList


def bTreeToCList(root):
    if (root == None):
        return None
    left = bTreeToCList(root.left)
    right = bTreeToCList(root.right)
    root.left = root
    root.right = root
    return concatenate(concatenate(left, root), right)


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        return bTreeToCList(A)
