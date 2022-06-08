
def subUnsort(A):
    n = len(A)
    smallest = -1
    largest = -1
    min_incorrect = float("Inf")
    max_incorrect = float("-Inf")
    isSorted = True

    # find minimum value which is incorrect
    for i in range(0, n - 1):
        if A[i] <= A[i + 1]:
            continue

        isSorted = False
        min_incorrect = min(min_incorrect,  A[i + 1])

    # find max value which is incorrect
    for i in range(n-1, 0, -1):
        if A[i - 1] <= A[i]:
            continue

        max_incorrect = max(A[i - 1], max_incorrect)

    if isSorted:
        return [-1]

    for i in range(0, n):
        if A[i] > min_incorrect:
            smallest = i
            break

    for i in range(n - 1, -1, -1):
        if A[i] < max_incorrect:
            largest = i
            break

    return [smallest, largest]


print(subUnsort([1, 2, 3, 5, 6, 13, 15, 16, 17,
      13, 13, 15, 17, 17, 17, 17, 17, 19, 19]))
