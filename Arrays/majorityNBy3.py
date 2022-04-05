
def repeatedNumber(A):

    first = -1
    second = -1
    count = 0
    count1 = 0

    for i in range(len(A)):

        if first == A[i]:
            count += 1
        elif second == A[i]:
            count1 += 1
        elif count == 0:
            count = 1
            first = A[i]
        elif count1 == 0:
            count1 = 1
            second = A[i]
        else:
            count -= 1
            count1 -= 1

    count = 0
    count1 = 0
    for i in range(len(A)):
        if A[i] == first:
            count += 1
        elif A[i] == second:
            count1 += 1
    
    if count > (len(A) / 3):
        return first
    
    if count1 > (len(A) / 3):
        return second

    return -1
 
# Driver code
arr = [ 1000938, 1000346, 1000346, 1000346, 1000561, 1000664, 1000671, 1000222, 1000702, 1000346, 1000346, 1000160, 1000958, 1000895 ]
n = len(arr)
print(repeatedNumber(arr))