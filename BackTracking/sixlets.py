# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     target = 1000
#     res = 0

#     def solve(self, A, B):
#         self.gen(A, B, 0, 0, 0)
#         return self.res

#     def gen(self, A, B, s,  size, indx):

#         if s > self.target:
#             return

#         if size == B:
#             self.res += 1
#             return

#         if indx == len(A):
#             return

#         for i in range(indx, len(A)):
#             self.gen(A, B, s + A[i], size + 1, i + 1)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    target = 1000

    def solve(self, A, B):
        return self.gen(A, B, 0, 0, 0)

    def gen(self, A, B, s, size, indx):

        if s > self.target:
            return 0

        if size == B:
            return 1

        if indx >= len(A):
            return 0

        return self.gen(A, B, s,  size, indx + 1) + self.gen(A, B, s + A[indx], size + 1, indx + 1)


print(Solution().solve([5, 17, 1000, 11], 4))
