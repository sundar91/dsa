import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        q = []
        A.sort(reverse=True)
        B.sort(reverse=True)

        res = []
        hs = set()
        n = len(A)

        # adding -ve sign will make it max heap
        heapq.heappush(q, (-(A[0] + B[0]), 0, 0))
        while len(q) > 0:
            val, i, j = heapq.heappop(q)

            res.append(-1 * val)

            s1 = str(i + 1) + "_" + str(j)
            s2 = str(i) + "_" + str(j + 1)

            if i + 1 < n and (s1 not in hs):
                hs.add(s1)
                heapq.heappush(q, (-(A[i+1] + B[j]), i + 1, j))

            if j + 1 < n and (s2 not in hs):
                hs.add(s2)
                heapq.heappush(q, (-(A[i] + B[j+1]), i, j + 1))

            if len(res) == len(A):
                break

        return res
