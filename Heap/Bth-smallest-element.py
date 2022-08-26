class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        m = len(A[0])
        h = []
        for i in range(n):
            for j in range(m):
                if len(h) < B:
                    h.append(A[i][j])
                    continue

                self.buildMaxHeap(h, len(h))
                self.insert(h, A[i][j])

        return h[0]

    def buildMaxHeap(self, A, n):
        start = (n - 2) // 2
        for i in range(start, -1, -1):
            self.heapify(A, n, i)

    def insert(self, A, num):
        if num < A[0]:
            A[0] = num

    def heapify(self, A, n, i):

        while i < n:
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < n and A[left] > A[largest]:
                largest = left

            if right < n and A[right] > A[largest]:
                largest = right

            if largest == i:
                break

            A[largest], A[i] = A[i], A[largest]
            i = largest


print(Solution().solve(
    [
        [6, 9, 13, 14, 18, 21, 25],
        [9, 11, 15, 18, 22, 24, 26],
        [10, 13, 18, 21, 25, 28, 31],
        [12, 15, 22, 24, 26, 31, 32],
        [16, 17, 25, 28, 32, 34, 35]
    ], 10))
