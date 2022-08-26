class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    A[i][j] += A[i][j - 1]
                elif j == 0:
                    A[i][j] += A[i - 1][j]
                else:
                    A[i][j] += min(A[i][j - 1], A[i - 1][j])
        return A[i][j]
