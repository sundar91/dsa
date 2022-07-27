class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        self.buildHeap(A, len(A))

        res = 0
        n = len(A)
        for i in range(n-1):

            a = A[0]
            last = A[n-1]
            A[0] = last
            n -= 1
            self.heapify(A, n, 0)
            b = A[0]
            A[0] = a + b
            self.heapify(A, n, 0)
            res += a + b
        return res

    def heapify(self, A, n, i):
        smallest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and A[left] < A[smallest]:
            smallest = left

        if right < n and A[right] < A[smallest]:
            smallest = right

        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]

            self.heapify(A, n, smallest)

    def buildHeap(self, A, n):
        index = n // 2 - 1
        for i in range(index, -1, -1):
            self.heapify(A, n, i)


print(Solution().solve([1, 2, 3, 4, 5]))
