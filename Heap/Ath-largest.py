# Given an integer array B of size N.

# You need to find the Ath largest element in the subarray[1 to i], where i varies from 1 to N. In other words, find the Ath largest element in the sub-arrays
# [1: 1], [1: 2], [1: 3], ...., [1: N].

# NOTE: If any subarray[1: i] has less than A elements, then the output should be - 1 at the ith index.

class Solution:

    def solve(self, A, B):
        n = len(B)
        h = []
        res = []
        for i in range(n):
            if i < A:
                h.append(B[i])
                self.parentHeapify(h, len(h) - 1)
                if A == len(h):
                    res.append(h[0])
                else:
                    res.append(-1)
            else:
                if B[i] > h[0]:
                    h[0] = B[i]
                    self.heapify(h, 0)

                res.append(h[0])

        return res

    def parentHeapify(self, A, index):
        while index > 0:
            pi = (index - 1) // 2
            if A[pi] > A[index]:
                A[pi], A[index] = A[index], A[pi]
                index = pi
            else:
                break

    def heapify(self, A, index):
        n = len(A)
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
            smallest = index


print(Solution().solve(4, [1, 2, 3, 4, 5, 6]))
