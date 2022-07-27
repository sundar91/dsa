class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        res = [-1, -1]
        n = len(A)

        if n == 1:
            return [-1]

        if n == 2:
            return [-1, -1]

        indx = n // 2

        h = []
        for i in range(n):
            self.insert(h, A[i])
            if i > 1:
                l = len(h)
                m3 = h[2]
                
                m3 = max(h[2], h[3], h[4])
                p = h[0] * h[1] * h[2]
                res.append(p)

        return res

    def insert(self, A, num):
        indx = len(A)
        A.append(num)

        while indx > 0:

            pi = (indx - 1) // 2
            if A[indx] > A[pi]:
                A[indx], A[pi] = A[pi], A[indx]
                indx = pi
            else:
                break


print(Solution().solve([1, 2, 3, 4, 5]))
