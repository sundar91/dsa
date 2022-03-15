def maxSubarray(A, B, C):
    max_sum = 0
    s = 0
    for i in range(0, A):
        s = 0
        for j in range(i, A):
            s += C[j]
            if s <= B and max_sum < s:
                max_sum = s
        
    return max_sum