class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):

        res, curr = [], []
        n = len(A)

        def dfs(i, s):

            if s == 0:
                res.append(curr.copy())
                return

            if i >= n or A[i] > s:
                return

            curr.append(A[i])
            dfs(i, s - A[i])
            curr.pop()
            dfs(i+1, s)

        dfs(0, B)

        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
