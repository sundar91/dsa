# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        prev = root
        while prev and prev.left:
            current = prev.left
            temp = current

            while current:
                current.next = prev.right
                prev = prev.next
                current = current.next
                if prev is None:
                    break

                current.next = prev.left
                current = current.next

            prev = temp


root = TreeLinkNode(1)
l1 = TreeLinkNode(2)

r1 = TreeLinkNode(3)

root.left = l1
root.right = r1

print(Solution().connect(root))
