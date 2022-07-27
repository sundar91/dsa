# We want to make a custom contacts finder applications as part of our college project. The application must perform two types of operations:

# Type 1: Add name B[i] ,denoted by 0 in vector A where B[i] is a string in vector B denoting a contact name. This must store B[i] as a new contact in the application.

# Type 2: Find partial for B[i] ,denoted by 1 in vector A where B[i] is a string in vector B denoting a partial name to search the application for. It must count the number of contacts starting with B[i].

# You have been given sequential add and find operations. You need to perform each operation in order.

# And return as an array of integers, answers for each query of type 2(denoted by 1 in A) .

# Input 1:

# A = [0, 0, 1, 1]
# B = ["hack", "hacker", "hac", "hak"]

# Output 1:

# [2, 0]

class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 1  # store how many strings crossed this node


class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def __init__(self):
        self.root = TrieNode()

    def solve(self, A, B):
        res = []
        for i in range(len(A)):
            if A[i] == 0:
                self.insert(B[i])
            elif A[i] == 1:
                res.append(self.search(B[i]))

        return res

    def search(self, s):
        current = self.root
        res = 0
        for i in range(len(s)):
            if not s[i] in current.child:
                return 0

            res = current.child[s[i]].count

            current = current.child[s[i]]

        return res

    def insert(self, s):
        current = self.root

        for i in range(len(s)):
            if not s[i] in current.child:
                current.child[s[i]] = TrieNode()
            else:
                current.child[s[i]].count += 1

            current = current.child[s[i]]
