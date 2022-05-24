# We have a list A of points (x, y) on the plane. Find the B closest points to the origin (0, 0).

# Here, the distance between two points on a plane is the Euclidean distance.

# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in.)

# NOTE: Euclidean distance between two points P1(x1, y1) and P2(x2, y2) is
# sqrt( (x1-x2)2 + (y1-y2)2 ).

from functools import cmp_to_key


def dict(item):
    return (item[0] * item[0]) + (item[1] * item[1])


def compare(x, y):
    if dict(x) > dict(y):
        return 1  # swap
    if dict(x) < dict(y):
        return -1  # don't swap
    return 0


def solve(A, B):
    A = sorted(A, key=cmp_to_key(compare))
    ans = []
    for i in range(B):
        ans.append(A[i])

    return ans


print(solve([
    [1, 3],
    [-2, 2]
], 1))
