class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):

        res, current = [], []

        n = len(A)
        A.sort()

        def dfs(pos, total):
            if total == 0:
                res.append(current.copy())
                return

            if pos >= n or total < 0:
                return

            prev = -1
            for i in range(pos, n):
                if prev == A[i]:
                    continue

                current.append(A[i])
                dfs(i + 1, total - A[i])
                current.pop()
                prev = A[i]

        dfs(0, B)
        return res
