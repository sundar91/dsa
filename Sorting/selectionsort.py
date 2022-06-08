def sort(A):
    n = len(A)
    for i in range(n):
        minIndex = i
        minValue = A[i]
        for j in range(i, n):
            if minValue > A[j]:
                minIndex = j
                minValue = A[j]

        if minIndex != i:
            A[minIndex], A[i] = A[i], A[minIndex]

    return A


print(sort([4, 2, 8, 6, 3, 1]))
