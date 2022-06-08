def sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]

    return A


print(sort([4, 2, 8, 6, 3, 1]))
