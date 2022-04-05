class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        a = [[0]*A for  i in range(A)]
        m = len(B)
        res = []
        sum = 0 
        for i in range(m):
            if B[i][0] == 1:
                res.append(sum)
            elif B[i][0] == 2:
                 r = B[i][1] - 1
                 c = B[i][2] - 1
                 if 1 - a[r][c] == 0 and sum > 0:
                    sum -= 1
                 else:
                     sum += 1
                 a[r][c] = 1 - a[r][c]
            elif B[i][0] == 3:
                 r= B[i][1] - 1
                 for j in range(A):
                     a[r][j] =  1 - a[r][j]
                     if a[r][j] == 0 and sum > 0:
                         sum -= 1
                     else:
                         sum += 1
        return res