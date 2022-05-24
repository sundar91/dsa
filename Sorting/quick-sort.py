import random


class Solution:
    def solve(self, A):
        self.qsort(A, 0, len(A) - 1)
        return A

    def qsort(self, A, s, e):
        if s >= e:
            return

        p = self.partition(A, s, e)
        self.qsort(A, s, p-1)
        self.qsort(A, p + 1, e)

    def partition(self, A, s, e):
        # randomizing pivot to improve worst case O(N^2)
        pivotIndex = random.randint(s, e)
        if pivotIndex != s:
            A[s], A[pivotIndex] = A[pivotIndex], A[s]

        p1, p2 = s + 1,  e
        while p1 <= p2:
            if A[p1] <= A[s]:
                p1 += 1
            elif A[p2] > A[s]:
                p2 -= 1
            else:
                A[p1], A[p2] = A[p2], A[p1]
                p1 += 1
                p2 -= 1

        A[s], A[p2] = A[p2], A[s]
        return p2
