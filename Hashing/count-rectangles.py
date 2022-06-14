# Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in a 2-D Cartesian plane.

# Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l])
# form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.
# Run two loops by fixing the two diagonally opposite rectangle ends.

# We have fixed the one diagonal of the rectangle and two corner points. From this, we can easily find the other two rectangle points.

# Suppose we have two diagonally opposite points: (x1, y1) and (x2, y2). Then the other two points of the rectangle must be (x1, y2) and (x2, y1).

# We have to check if these two points (x1, y2) and (x2, y1) are given or not. If present, increment the answer.

# We have incremented the answer twice for every rectangle because every rectangle has two diagonals. So, our final answer will be half of the answer obtained after running two loops.
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        h = set()
        n = len(A)
        for i in range(n):
            h.add((A[i], B[i]))

        count = 0

        for i in range(n):
            fx = A[i]
            fy = B[i]
            for j in range(i + 1, n):
                sx = A[j]
                sy = B[j]

                # ignore same side points as need to focus on diagnols
                if sx == fx or sy == fy:
                    continue

                if (fx, sy) in h and (sx, fy) in h:
                    count += 1
        return count // 2
