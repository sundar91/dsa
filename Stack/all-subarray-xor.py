from collections import deque


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        ngl = self.nextGreaterLeft(A)
        ngr = self.nextGreaterRight(A)

        res = float('-inf')

        print(ngl)
        print(ngr)

        for i in range(len(A)):
            l = ngl[i]
            r = ngr[i]

            if l != -1:
                x = l ^ A[i]
                res = max(res, x)

            if r != -1:
                x = r ^ A[i]
                res = max(res, x)

        return res

    def nextGreaterLeft(self, A):
        n = len(A)
        ngl = [-1] * n
        stack = []

        for i in range(n):
            val = A[i]
            while len(stack) > 0 and stack[-1] <= val:
                stack.pop()

            if len(stack) > 0:
                ngl[i] = stack[-1]

            stack.append(val)

        return ngl

    def nextGreaterRight(self, A):
        n = len(A)
        ngr = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            val = A[i]

            while len(stack) > 0 and stack[-1] <= val:
                stack.pop()

            if len(stack) > 0:
                ngr[i] = stack[-1]

            stack.append(val)

        return ngr


class Solution2:
    def solve(self, A):
        n = len(A)
        s = []
        res = 0

        for i in range(n):
            while len(s):
                top = s[-1]

                res = max(res, A[top] ^ A[i])

                if top > A[i]:
                    break

                s.pop()

            s.append(i)

        return res


print(Solution2().solve([9, 3, 2, 8, 2, 1, 4]))
