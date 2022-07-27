
from collections import defaultdict
import re


class TrieNode():
    def __init__(self):
        self.child = defaultdict()

        self.end = False
        self.words = []
        self.order = 0
        self.count = 1


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def solve(self, A, order, B, n, m):

        # Build Trie node
        for i in range(n):
            self.insert(A[i], order[i])

        for i in range(m):
            d = self.search(B[i])
            print(d)
            # if len(d) == 0:
            #     print(-1, end=' ')
            # else:
            #     for j in range(len(d)):
            #         print(d[j][0], end=' ')

            print('')

    def search(self, s):
        current = self.root
        res = []
        for i in range(len(s)):
            if s[i] not in current.child:
                return []
            current = current.child[s[i]]

        return current.words

    def insert(self, s, order):
        current = self.root
        for i in range(len(s)):
            if not s[i] in current.child:
                current.child[s[i]] = TrieNode()

            current = current.child[s[i]]
            if len(current.words) < 5:
                current.words.append((s, order))
                j = len(current.words) - 1
                while j > 0 and current.words[j][1] > current.words[j-1][1]:
                    current.words[j], current.words[j -
                                                    1] = current.words[j-1], current.words[j]
                    j -= 1

            else:
                n = len(current.words)
                j = n - 1
                if order > current.words[-1][1]:
                    current.words[j] = (s, order)
                    while j > 0 and current.words[j][1] > current.words[j-1][1]:
                        current.words[j], current.words[j -
                                                        1] = current.words[j-1], current.words[j]
                        j -= 1

        current.order = order
        if current.end:
            current.count += 1
        current.end = True


Solution().solve(['abcd', 'aecd', 'abaa', 'abef', 'acdcc', 'acbcc'], [
    2, 1, 3, 4, 6, 5], ['ab', 'abc', 'a'], 6, 3)
