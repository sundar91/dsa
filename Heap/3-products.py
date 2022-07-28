
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

        h, k = [], 3
        for i in range(k):
            h.append(A[i])

        self.heapify(h, k, 0)

        for i in range(k, n):
            p = h[0] * h[1] * h[2]
            res.append(p)
            self.insert(h, A[i])

        p = h[0] * h[1] * h[2]
        res.append(p)

        return res

    # to find top k largest element we can create min heap and each time for new element
    # we can compare if that can be be largest, as smallest will be at root
    def insert(self, A, num):
        if num > A[0]:
            A[0] = num
            self.heapify(A, len(A), 0)

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
            smallest = i


print(Solution().solve([10, 2, 13, 4]))
