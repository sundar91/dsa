from collections import deque


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        h = {}
        q = deque()
        res = []
        for i in range(len(A)):
            val = A[i]
            h[val] = 1 + h.get(val, 0)

            if len(q) > 0 and q[0] == val:
                q.popleft()

            # remove all occurence of repeated characters from front
            while len(q) > 0 and h[q[0]] > 1:
                q.popleft()

            if h[val] == 1:
                q.append(val)

            if len(q) == 0:
                res.append('#')
            else:
                res.append(q[0])

        return ''.join(res)


print(Solution().solve('abaddbc'))
