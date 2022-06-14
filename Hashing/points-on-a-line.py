def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def maxpointsonsameline(x, y):
    n = len(x)
    if n < 3:
        return n
    ans = 0
    curmax = 0
    overlap = 0
    vertical = 0
    for i in range(n):
        mp = {}
        curmax = 0
        overlap = 0
        vertical = 0
        for j in range(i + 1, n):
            if x[i] == x[j] and y[i] == y[j]:
                overlap += 1
            elif x[i] == x[j]:
                vertical += 1
            else:
                xdiff = x[j] - x[i]
                ydiff = y[j] - y[i]
                z = gcd(xdiff, ydiff)
                xdiff /= z
                ydiff /= z
                if mp.get((xdiff, ydiff)) == None:
                    mp[(xdiff, ydiff)] = 1
                else:
                    mp[(xdiff, ydiff)] += 1
                curmax = max(curmax, mp[(xdiff, ydiff)])
            curmax = max(curmax, vertical)
        ans = max(ans, curmax + overlap + 1)
    return ans
