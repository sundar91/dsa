# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

# Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.

# NOTE: The answer may be large so return the answer modulo (109 + 7).

# HINT :
# Try fixing each point as the intersection of perpendicular and base and finding other points.

# Once it is fixed, for the other two points, one point will share the same x-coordinate, and the other point will share the same
# y-coordinate with the selected point.

# We can use a map to store the points for points sharing the same x or y coordinate.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        ha = {}
        hb = {}

        mod = pow(10, 9) + 7

        for i in range(n):
            val = A[i]
            ha[val] = 1 + ha.get(val, 0)

            y = B[i]
            hb[y] = 1 + hb.get(y, 0)

        count = 0
        for i in range(n):
            x = A[i]
            y = B[i]
            count += ((ha[x] - 1) * (hb[y] - 1)) % mod

        return count % mod
