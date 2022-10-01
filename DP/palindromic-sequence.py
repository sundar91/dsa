class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):

        n = len(A)

        # aba 0 (already a palindrome)
        # aab 1 (aa and b needs a cut)
