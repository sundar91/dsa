from turtle import circle


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.res = []

    def permute(self, A):
        self.gen(A, 0)
        return self.res

    def gen(self, A, indx):
        if indx == len(A) - 1:
            self.res.append(A.copy())
            return

        for i in range(indx, len(A)):
            A[i], A[indx] = A[indx], A[i]
            self.gen(A, indx + 1)
            # undo
            A[i], A[indx] = A[indx], A[i]


class Solution2:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.res = []

    def permute(self, A):
        hs = set()
        self.gen(A, [], 0, hs)
        return self.res

    def gen(self, A, current, indx, hs):
        if indx == len(A):
            self.res.append(current.copy())
            return

        for i in range(0, len(A)):
            if A[i] not in hs:
                current.append(A[i])
                hs.add(A[i])
                self.gen(A, current, indx + 1, hs)
                hs.remove(A[i])
                current.pop()


print(Solution2().permute([1, 2, 3]))
