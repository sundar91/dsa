from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict()
        self.number_of_child_0 = 0
        self.number_of_child_1 = 0


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.root = TrieNode()

    def solve(self, A, B):

        cummulative_xor = 0
        res = 0
        mod = int(1e9+7)

        self.insert(cummulative_xor)
        for i in range(len(A)):
            cummulative_xor ^= A[i]
            res += self.search(cummulative_xor, B)
            self.insert(cummulative_xor)
            res %= mod

        return res

    def search(self, num, B):
        current = self.root
        msb = 31
        ans = 0
        mod = int(1e9+7)

        while msb >= 0:

            currentBit = 1 & (num >> msb)
            currentBBit = 1 & (B >> msb)
            if currentBBit == 1:
                if currentBit == 0:
                    ans = (ans + current.number_of_child_0) % mod
                    if 1 not in current.child:
                        return ans
                    current = current.child[1]
                else:
                    ans = (ans + current.number_of_child_1) % mod
                    if 0 not in current.child:
                        return ans
                    current = current.child[0]
            else:

                if currentBit not in current.child:
                    return ans
                current = current.child[currentBit]

            msb -= 1

        return ans

    def insert(self, num):
        current = self.root
        msb = 31
        while msb >= 0:
            bit = 1 & (num >> msb)

            if bit == 0:
                current.number_of_child_0 += 1
            else:
                current.number_of_child_1 += 1

            if bit not in current.child:
                current.child[bit] = TrieNode()

            current = current.child[bit]
            msb -= 1
