
def findMedian(A):

    n = len(A)
    m = len(A[0])
    K = (n * m) // 2

    low, high = getMinMax(A)
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        s = 0
        for i in range(n):
            s += findCount(A[i], mid)

        if s <= K:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


def getMinMax(matrix):
    min_el = float('inf')
    max_el = float('-inf')
    for row in matrix:
        if min_el > row[0]:
            min_el = row[0]
        if max_el < row[-1]:
            max_el = row[-1]

    return min_el, max_el


def findCount(A, B):
    low, high = 0, len(A) - 1

    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < B:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans + 1


print(findMedian([[5], [4], [3], [1], [3], [1], [4], [2], [5], [3], [3]]))

print(findMedian([[9, 10, 10, 13, 14, 15, 16, 16, 16, 17, 18], [
      1, 4, 9, 14, 16, 18, 19, 22, 26, 26, 27], [4, 6, 7, 10, 14, 20, 21, 23, 24, 27, 28]]))

print(findMedian([[5, 17, 100]]))
print(findMedian([[1, 3, 5], [2, 6, 9], [3, 6, 9]]))
