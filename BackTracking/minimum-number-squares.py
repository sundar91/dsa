count = 0


def countMinSquares(A):
    global count
    if A <= 3:
        count += A
        return A

    p = findClosestPerfectSquare(A)
    A = A - (p * p)
    count += 1
    countMinSquares(A)


def findClosestPerfectSquare(num):
    low, high = 1, num

    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid == num:
            ans = mid
            break

        if mid * mid <= num:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


countMinSquares(12)
print(count)
