def alternatingArray(A, k):
    left = [0] *len(A)
    right = [0] * len(A)

    count = 1
    left[0] = 1 
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            count += 1
        else:
            count = 1

        left[i] = count

    right[len(A) - 1] = 1
    count = 1
    for i in range(len(A)-2,-1, -1):
        if A[i] != A[i+1]:
            count += 1
        else:
            count = 1

        right[i] = count

    
    
    return (left,right)

print(alternatingArray([1,0,1,0,1,1], 1))

        
