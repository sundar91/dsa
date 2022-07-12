class Solution:
    ans = 1

    def findDepth(self, node, depth):
        if node == None:
            return depth - 1
        lt_dt = self.findDepth(node.left, depth + 1)
        rt_dt = self.findDepth(node.right, depth + 1)
        if abs(lt_dt - rt_dt) > 1:
            self.ans = 0
        return max(lt_dt, rt_dt)

    def isBalanced(self, A):
        self.findDepth(A, 0)
        return self.ans
