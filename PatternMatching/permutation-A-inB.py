# You are given two strings, A and B, of size N and M, respectively.

# You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.


# i/p :
#  A = "abc"
#  B = "abcbacabc"

#  o/p : 5

#  Permutations of A that are present in B as substring are:
#     1. abc
#     2. cba
#     3. bac
#     4. cab
#     5. abc
#     So ans is 5.


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        hA = {}
        hB = {}
        count = 0
        for a in A:
            hA[a] = 1 + hA.get(a, 0)

        n = len(A)

        for i in range(n):
            val = B[i]
            hB[val] = 1 + hB.get(val, 0)

        if self.isPermutation(hA, hB):
            count += 1

        for i in range(1, len(B) - n + 1):
            val = B[i + n - 1]
            r = B[i-1]
            hB[r] -= 1
            hB[val] = 1 + hB.get(val, 0)
            if self.isPermutation(hA, hB):
                count += 1

        return count

    def isPermutation(self, h1, h2):
        for v in h1:
            if (not v in h2) or h2[v] != h1[v]:
                return False

        return True
