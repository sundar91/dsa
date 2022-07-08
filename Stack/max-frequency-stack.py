# Problem Description
# You are given a matrix A which represents operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it.

# Operations are of two types:

# 1 x: push an integer x onto the stack and return -1.

# 2 0: remove and return the most frequent element in the stack.

# If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.

# A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.

from collections import defaultdict


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        numFreq = {}
        freqStack = defaultdict(lambda: [])
        res = []
        maxFreq = 0

        def push(num):
            nonlocal maxFreq

            numFreq[num] = 1 + numFreq.get(num, 0)
            freq = numFreq[num]
            if freq > maxFreq:
                maxFreq = freq

            freqStack[freq].append(num)

        def pop():
            nonlocal maxFreq
            if maxFreq == 0:
                return -1

            val = freqStack[maxFreq].pop()

            if len(freqStack[maxFreq]) == 0:
                maxFreq -= 1

            numFreq[val] -= 1
            if numFreq[val] == 0:
                del numFreq[val]

            return val

        for i in range(len(A)):
            if A[i][0] == 1:
                push(A[i][1])
                res.append(-1)
            else:
                val = pop()
                res.append(val)

        return res


arr = [
    [1, 5],
    [1, 7],
    [1, 5],
    [1, 7],
    [1, 4],
    [1, 5],
    [2, 0],
    [2, 0],
    [2, 0],
    [2, 0]
]
print(Solution().solve(arr))
