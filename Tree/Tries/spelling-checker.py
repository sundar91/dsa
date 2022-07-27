class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        root = self.insertDictionary(A)

        res = []
        # check if each character is in the node
        for i in range(len(B)):
            current = root
            flag = False
            for j in range(len(B[i])):
                s = B[i][j]
                if not s in current.child:
                    flag = True
                    break

                current = current.child[s]

            if flag:
                res.append(0)
            else:
                res.append(int(current.end))

        return res

    def insertDictionary(self, A):
        dummy = TrieNode()

        for i in range(len(A)):
            current = dummy
            for j in range(len(A[i])):
                s = A[i][j]
                if not s in current.child:
                    current.child[s] = TrieNode()

                current = current.child[s]

            current.end = True

        return dummy
