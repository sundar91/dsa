def solve(A):
    lower, upper = float('-inf'), float('inf')

    prev = A[0]
    for i in range(1, len(A)):
        if not lower <= A[i] <= upper:
            return "NO"

        if A[i] < prev:
            upper = prev - 1

        elif A[i] > prev:
            lower = prev + 1

        prev = A[i]

    return "YES"


print(solve([4, 10, 5, 8]))
