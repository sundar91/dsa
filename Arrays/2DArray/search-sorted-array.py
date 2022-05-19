class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])
        l, r = 0, n-1
        while l <= r:
            mid = int(l + ((r - l)/2))
            if A[mid][0] == B:
                return (mid + 1) * 1009 + 1

            if A[mid][m-1] == B:
                return (mid + 1) * 1009 + m

            if B > A[mid][0] and B < A[mid][m-1]:
                col = self.binarySearch(A, B, m, mid)
                if col != -1:
                    return (mid + 1) * 1009 + (col + 1)

            if A[mid][0] < B:
                l = mid + 1
            if A[mid][m-1] > B:
                r = mid - 1

        return -1

    def binarySearch(self, A, B, m, row):

        l, r = 0, m-1
        while l <= r:
            mid = int(l + ((r-l)/2))

            if A[row][mid] == B:
                return mid

            if A[row][mid] < B:
                l = mid + 1
            else:
                r = mid - 1

        return -1
