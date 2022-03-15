def solve(A, B):
    currentSum = 0
    for i in range(0, B):
        currentSum += A[i]
    
    avg = currentSum / B
    start_index = 0
    n = len(A)
    for i in range(1, n - B + 1):
        currentSum = currentSum - A[i-1] + A[i + B - 1]
        currentAvg = (currentSum / B) 
        if avg > currentAvg: 
            avg = currentAvg
            start_index = i
    return start_index

print(solve([ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ], 9))