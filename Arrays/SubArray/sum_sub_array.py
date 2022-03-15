def sumSubArray(A):
    s = 0
    for i in range(0,len(A)):
        c = (i+1) *(len(A) -i)
        s +=  c * A[i]
    return s

print(sumSubArray([1, 2, 3]))
