def maxProfit(prices) -> int:
    last_max = -float("Inf")
    last_min = float("Inf")
    for i in range(0, len(prices)):
        
        if last_min > prices[i]:
            last_min = prices[i]
        
        if last_min < prices[i] and last_max < prices[i]:
            last_max = prices[i]
    
    if last_max == -float("Inf") or last_min == float("Inf"):
        return 0
    return  last_max - last_min


def solve(A):
    max = -float("Inf")
    min = float("Inf")
    for i in range(0, len(A)):
        if max < A[i]:
            max = A[i]
        if min > A[i]:
            min = A[i]

    last_max = -1
    last_min = -1
    l = 0
    for i in range(0, len(A)):
        if A[i] == max:
            last_max = i
        if A[i] == min:
            last_min = i

        l = max(l, last_max)
    return l    


# print(maxProfit([7,1,5,3,6,4]))

print(solve([ 814, 761, 697, 483, 981 ]))