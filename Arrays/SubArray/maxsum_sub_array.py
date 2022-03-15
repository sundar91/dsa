def maxSumArray(A):
    s = 0,
    max_sum = 0
    for i in range(0, len(A)):
        s = max(s + A[i],A[i])
        max_sum = max(s, max_sum)
    return max_sum