class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        h = []
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                p, q = A[i], A[j]
                if len(h) == B:
                    if (p / q) < h[0][0]:
                        h[0] = (p/q, p, q)
                        self.heapify(h, 0)
                else:
                    h.append((p/q, p, q))
                    self.childHeapify(h, len(h)-1)

        return [h[0][1], h[0][2]]

    def childHeapify(self, A, index):
        while index > 0:
            parent = (index-1)//2
            if A[parent][0] < A[index][0]:
                A[parent], A[index] = A[index], A[parent]
                index = parent
            else:
                break

    def heapify(self, A, index):

        n = len(A)
        while index < n:

            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and A[left][0] > A[largest][0]:
                largest = left

            if right < n and A[right][0] > A[largest][0]:
                largest = right

            if largest == index:
                break

            A[largest], A[index] = A[index], A[largest]
            index = largest


print(Solution().solve([1, 719, 983, 9293, 11321,
      14447, 16411, 17881, 22079, 28297], 42))
