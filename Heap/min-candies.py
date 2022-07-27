class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        self.buildMinHeap(A)
        count = 0
        n = len(A)
        while n:
            minCandies = A[0]
            if minCandies > B:
                break

            count += (minCandies // 2)
            A[0] = A[n-1]
            n = n - 1
            self.heapify(A, n, 0)
            A[0] += minCandies - (minCandies // 2)
            self.heapify(A, n, 0)

        return count

    def buildMinHeap(self, A):
        n = len(A)
        start = (n-2) // 2
        for i in range(start, -1, -1):
            self.heapify(A, n, i)

    def heapify(self, A, n, i):

        while i < n:
            smallest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < n and A[left] < A[smallest]:
                smallest = left

            if right < n and A[right] < A[smallest]:
                smallest = right

            if smallest == i:
                break

            A[smallest], A[i] = A[i], A[smallest]
            i = smallest


print(Solution().solve([9, 818, 174, 237, 892, 109, 522, 27, 59, 336, 605, 865, 714, 86, 708, 535, 138, 948, 836, 287, 179, 754, 466, 856, 153,
      53, 958, 951, 262, 341, 769, 491, 772, 509, 336, 120, 98, 805, 169, 984, 520, 447, 256, 266, 348, 351, 60, 563, 45, 638, 29, 479, 400], 852))
