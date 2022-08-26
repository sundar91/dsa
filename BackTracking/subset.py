ans = []
curr = []


def solve(i, n, A):
    global ans, curr
    if i == n:
        ans.append(sorted(curr.copy()))
        return
    solve(i+1, n, A)
    curr.append(A[i])
    solve(i+1, n, A)
    curr.pop()


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        global ans, curr
        ans = []
        n = len(A)
        solve(0, n, A)
        return sorted(ans)


# res = []
# 	def subsets(self, A):
#         self.gen(A, [], 0)
#         return sorted(self.res)

#     def gen(self, A,  current, indx):
#         if indx == len(A):
#             self.res.append(sorted(current.copy()))
#             return

#         self.gen(A, current, indx + 1)
#         current.append(A[indx])
#         self.gen(A, current, indx + 1)
#         current.pop()


print(Solution().subsets([15, 20, 12, 19, 4]))
