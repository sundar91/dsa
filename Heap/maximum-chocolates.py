class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        B.sort(reverse=True)
        count = 0
        for i in range(A):
            count += B[0]
            B[0] = B[0] // 2
            self.convert(B, 0)

        return count

    def convert(self, A, i):
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(A)
        if i >= n:
            return

        # if A[i] > A[left] and A[i] > A[right]:
        #     return

        if left < n and A[i] < A[left] and (right >= n or (right < n and A[left] > A[right])):
            A[i], A[left] = A[left], A[i]
            i = left
        elif right < n and A[i] < A[right]:
            A[i], A[right] = A[right], A[i]
            i = right
        else:
            return

        self.convert(A, i)


print(Solution().nchoc(10, [2147483647, 2000000014, 2147483647]))
