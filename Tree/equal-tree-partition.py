
# Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.
import sys
sys.setrecursionlimit(1000000)


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        seen = set()

        def calcTotalSum(node):
            if node is None:
                return 0

            total = node.val + \
                calcTotalSum(node.left) + calcTotalSum(node.right)
            seen.add(total)
            return total

        total = calcTotalSum(A)

        if total // 2 in seen:
            return 1

        else:
            return 0
