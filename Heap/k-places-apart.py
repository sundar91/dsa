import heapq
from random import sample
from tracemalloc import start


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        h = []
        res = []

        i = 0

        while i <= B:
            h.append(A[i])
            i += 1

        self.buildHeap(h)

        while i < len(A):
            res.append(h[0])
            h[0] = A[i]
            self.heapify(h, len(h),  0)
            i += 1

        i = len(A) - B - 1
        count = 2
        while i != len(A):
            l = len(h) - count

            res.append(h[0])
            h[0] = h[l + 1]
            h[l+1] = res[-1]
            self.heapify(h, l + 1, 0)
            i += 1
            count += 1
        return res

    def buildHeap(self, A):
        n = len(A)
        start = n // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(A, n, i)

    def heapify(self, A, n,  index):
        while index < n:
            left = 2 * index + 1
            right = 2 * index + 2

            smallest = index

            if left < n and A[left] < A[smallest]:
                smallest = left

            if right < n and A[right] < A[smallest]:
                smallest = right

            if smallest == index:
                break

            A[smallest], A[index] = A[index], A[smallest]
            index = smallest


# using priority queue inbuild
class Solution2:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        pq = []
        i = 0
        n = len(A)

        # insert first B+1 elements in the priority queue.
        while(i <= min(B, n-1)):
            heapq.heappush(pq, A[i])
            i += 1

        # Keep on removing the minimum element from the queue
        j = 0
        while(i < n):
            A[j] = heapq.heappop(pq)
            heapq.heappush(pq, A[i])
            i += 1
            j += 1

        while(j < n):
            A[j] = heapq.heappop(pq)
            j += 1

        return A


# print(Solution().solve([25, 16, 11, 31, 28, 20, 3, 8], 6))
print(Solution().solve([8, 3, 12], 1))
