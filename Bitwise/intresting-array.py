# You have an array A with N elements. We have two types of operation available on this array :
# We can split an element B into two elements, C and D, such that B = C + D.
# We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
# You have to determine whether it is possible to convert array A to size 1, 
# containing a single element equal to 0 after several splits and/or merge?


# Hint:  if no. of elements are odd then it is not possible to generate 0.
def solve(A):
    if len(A) <= 1:
        return "No"
    
    xr = A[0]
    for i in range(1, len(A)):
        xr ^= A[i]

    if xr % 2 == 0:
        return "Yes"
    else:
        return "No" 

print(solve([1]))