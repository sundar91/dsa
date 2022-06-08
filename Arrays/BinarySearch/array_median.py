class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        low, high = 0, len(A) - 1
        total_len = len(A) + len(B)
        k = total_len // 2

        while True:

            mid = (low + high) // 2
            j = k - mid - 2

            ALeft = A[mid] if mid >= 0 else float('-Inf')
            ARight = A[mid + 1] if (mid + 1) < len(A) else float('Inf')
            BLeft = B[j] if j >= 0 else float('-Inf')
            BRight = B[j + 1] if (j + 1) < len(B) else float('Inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total_len % 2 == 0:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                else:
                    return min(ARight, BRight)
            elif ALeft > BRight:
                high = mid - 1
            else:
                low = mid + 1
