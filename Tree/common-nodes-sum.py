# Optimized approach with iterative inorder traversal
mod = 1000000007


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solveQ(root1, root2):
    s1 = []
    s2 = []
    ans = 0
    while 1:
        if root1:
            s1.append(root1)
            root1 = root1.left
        elif root2:
            s2.append(root2)
            root2 = root2.left
        elif len(s1) != 0 and len(s2) != 0:
            root1 = s1[-1]
            root2 = s2[-1]
            if root1.val == root2.val:
                ans += root1.val
                ans %= mod
                s1.pop(-1)
                s2.pop(-1)
                root1 = root1.right
                root2 = root2.right
            elif root1.val < root2.val:
                s1.pop(-1)
                root1 = root1.right
                root2 = None
            elif root1.val > root2.val:
                s2.pop(-1)
                root2 = root2.right
                root1 = None
        else:
            break
    return ans


class Solution:
    def solve(self, A, B):
        ans = solveQ(A, B)
        return ans


# Trivial Approach creating two inorder traversal array and finding intersection of two arrays.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
mod = 1000000007


def inOrder(A, a):
    if A == None:
        return
    inOrder(A.left, a)
    a.append(A.val)
    inOrder(A.right, a)


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):
        a = []
        b = []
        inOrder(A, a)
        inOrder(B, b)
        i = 0
        j = 0
        n = len(a)
        m = len(b)
        ans = 0
        while i < n and j < m:
            if a[i] < b[j]:
                i += 1
            elif b[j] < a[i]:
                j += 1
            else:
                ans += a[i]
                ans %= mod
                i += 1
                j += 1
        return ans


root = TreeNode(5)
l1 = TreeNode(2)
l1.right = TreeNode(3)


r1 = TreeNode(8)
r2 = TreeNode(15)
r1.right = r2
r2.left = TreeNode(9)

root.left = l1
root.right = r1


root1 = TreeNode(7)
l12 = TreeNode(1)
l12.right = TreeNode(2)

r12 = TreeNode(10)
r22 = TreeNode(15)
r12.right = r22
r22.left = TreeNode(11)

root1.left = l12
root1.right = r12

print(Solution().solve(root, root1))
