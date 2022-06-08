def insertionsort(A):
    for i in range(1, len(A)):
        val = A[i]
        j = i - 1
        while j >= 0:
            if A[j] > val:
                A[j+1] = A[j]
                j -= 1
            else:
                break
        A[j+1] = val

    return A


print(insertionsort([4, 2, 8, 6, 3, 1]))
