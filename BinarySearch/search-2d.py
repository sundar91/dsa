class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[mid][0]

            if val == target:
                return True

            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        row = r
        print(row)

        l, r = 0, m - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[row][mid]

            if val == target:
                return True

            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
