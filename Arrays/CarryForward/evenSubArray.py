# You are given an integer array A.

# Decide whether it is possible to divide the array into one or more subarrays of even length such that first and last element 
# of all subarrays will be even.

# Return "YES" if it is possible otherwise return "NO" (without quotes).

def solve(A):
        if len(A)%2 == 0 and A[0]%2 == 0 and A[-1]%2 == 0: return "YES"
        return "NO"

print(solve([2, 4, 8, 6]))
print(solve([2, 4, 8, 7, 6]))