# Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A.
# Find the total number of inversions of A modulo (10^9 + 7).

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return self.invCount(A, 0, len(A) - 1)

    def invCount(self, A, s, e):
        if s == e:
            return 0

        mod = pow(10, 9) + 7

        m = int((s + e) / 2)
        x = self.invCount(A, s, m)
        y = self.invCount(A, m + 1, e)

        z = self.merge(A, s, m, e)

        return (x + y + z) % mod

    def merge(self, A, s, m, e):

        mod = pow(10, 9) + 7

        C = [0] * (e - s + 1)
        p1, p2, p3 = s, m + 1, 0
        cnt = 0

        while p1 <= m and p2 <= e:
            if A[p1] <= A[p2]:
                C[p3] = A[p1]
                p1 += 1
                p3 += 1
            else:
                C[p3] = A[p2]
                cnt += m - p1 + 1
                p2 += 1
                p3 += 1

        while p1 <= m:
            C[p3] = A[p1]
            p1 += 1
            p3 += 1

        while p2 <= e:
            C[p3] = A[p2]
            p2 += 1
            p3 += 1

        for i in range(0, len(C)):
            A[i + s] = C[i]

        return cnt % mod
