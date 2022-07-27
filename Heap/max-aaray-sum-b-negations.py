class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        self.buildMinHeap(A, len(A))
        for i in range(B):
            A[0] = A[0] * -1
            self.heapify(A, len(A), 0)

        s = 0
        print(A)
        for i in range(len(A)):
            s += A[i]

        return s

    def buildMinHeap(self, A, n):
        start = (n - 1) // 2
        for i in range(start, -1, -1):
            self.heapify(A, n, i)

    def heapify(self, A, n, index):

        while index < n:

            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if left < n and A[left] < A[smallest]:
                smallest = left

            if right < n and A[right] < A[smallest]:
                smallest = right

            if smallest == index:
                break

            A[index], A[smallest] = A[smallest], A[index]
            index = smallest


print(Solution().solve([57, 3, -14, -87, 42, 38, 31, -7, -28, -61], 1))
