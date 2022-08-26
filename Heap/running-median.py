class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        hmax = []
        hmin = []

        res = []
        for i in range(len(A)):
            hmax.append(A[i])
            n = len(hmax)
            m = len(hmin)
            self.maxHeapify(hmax, n - 1)
            element = hmax[0]

            if abs(n - m) > 1:
                hmax[0] = hmax[n - 1]
                hmax.pop()
                n = n - 1
                self.heapify(hmax, n, 0)

                hmin.append(element)
                self.minHeapify(hmin, len(hmin) - 1)

            elif len(hmin) > 0 and element > hmin[0]:
                hmax[0] = hmin[0]
                self.heapify(hmax, n, 0)

                hmin[0] = element
                self.heapifyMin(hmin, len(hmin), 0)

            res.append(hmax[0])

        return res

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

    def heapifyMin(self, A, n, i):
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

    def maxHeapify(self, A, i):
        while i > 0:
            parent = (i-1) // 2
            if A[i] > A[parent]:
                A[parent], A[i] = A[i], A[parent]
                i = parent
            else:
                break

    def minHeapify(self, A, i):
        while i > 0:
            parent = (i - 1) // 2
            if A[i] < A[parent]:
                A[i], A[parent] = A[parent], A[i]
                i = parent
            else:
                break


print(Solution().solve([ 59, 64, 10, 39 ])) 
