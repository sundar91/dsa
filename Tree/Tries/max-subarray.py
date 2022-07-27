import math
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict()
        self.index = 0
        self.val = 0


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def __init__(self):
        self.root = TrieNode()
        self.max_xor = 0
        self.res = [-1, -1]

    def solve(self, A):

        n = len(A)
        pf = [0] * n
        pf[0] = A[0]

        self.max_xor = A[0]
        self.res = [1, 1]
        for i in range(1, n):
            pf[i] = pf[i-1] ^ A[i]
            if A[i] > self.max_xor:
                self.max_xor = A[i]
                self.res = [i + 1, i + 1]
            if pf[i] > self.max_xor:
                self.max_xor = pf[i]
                self.res = [1, i + 1]

        max_value = max(pf)
        if max_value == 0:
            return 0

        print(pf)

        msb = int(math.log(max_value, 2))
        for i in range(n):
            self.insert(pf[i], i + 1,  msb)

        for i in range(n):
            self.search(pf[i], i + 1, msb)

        return sorted(self.res)

    def insert(self, num, index, msb):
        current = self.root
        i = msb
        while i >= 0:
            r = (num >> i) & 1

            if not r in current.child:
                current.child[r] = TrieNode()

            current = current.child[r]

            i -= 1

        current.index = index
        current.val = num

    def search(self, num, index,  msb):
        current = self.root
        i = msb
        while i >= 0:

            r = (num >> i) & 1
            notRes = 1 - r
            if notRes in current.child:
                current = current.child[notRes]
            else:
                current = current.child[r]

            i -= 1

        current_xor = current.val ^ num

        if current_xor == self.max_xor:
            prev_len = abs(self.res[1] - self.res[0])
            current_len = abs(current.index - index + 1)
            if current_len < prev_len:
                s, e = current.index, index
                if s > e:
                    s, e = e, s

                self.res[0] = s + 1
                self.res[1] = e

            return

        if self.max_xor < current_xor:
            self.max_xor = current_xor
            s, e = current.index, index
            if s > e:
                s, e = e, s
            self.res = [s + 1, e]


print(Solution().solve([37, 24, 17, 26, 37, 10, 15, 35, 7, 33]))

# [15, 25, 23]
