import random
N = 100000
INF = 1 << 46
Hash = {}


def rand46():  # generates 46bit random number
    ret = 0
    ret |= random.randint(0, INF)
    x = random.randint(0, INF)
    ret = ret | (x << 15)
    return ret


def set_hash(a):
    Hash.clear()
    n = len(a)
    for i in range(0, n):
        if Hash.get(a[i]) == None:  # consider multiple occurences
            Hash[a[i]] = rand46()


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        res = []
        n = len(A)

        set_hash(A)
        pf = [0] * n
        pf[0] = Hash[A[0]]
        for i in range(1, n):
            pf[i] = pf[i - 1] + Hash.get(A[i])

        for i in range(len(B)):
            l1, r1 = B[i][0], B[i][1]
            l2, r2 = B[i][2], B[i][3]

            if r1 - l1 != r2 - l2:
                res.append(0)
                continue

            if l1 == 0:
                left = pf[r1]
            else:
                left = pf[r1] - pf[l1 - 1]

            if l2 == 0:
                right = pf[r2]
            else:
                right = pf[r2] - pf[l2 - 1]

            if left == right:
                res.append(1)
            else:
                res.append(0)

        return res


print(Solution().solve([1, 7, 11, 8, 11, 7, 1], [[0, 2, 4, 6]]))
