# You are given a string A of length N consisting of lowercase alphabets. Find the period of the string.

# Period of the string is the minimum value of k (k >= 1), that satisfies A[i] = A[i % k] for all valid i.

# Example:
#  A = "abababab"

#  O/p : 2
#  Explanation : Period of the string will be 2: Since, for all i, A[i] = A[i%2].

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        lps = [0] * n

        for i in range(1, n):
            x = lps[i - 1]
            while A[x] != A[i]:
                if x == 0:
                    x = -1
                    break
                x = lps[x-1]

            lps[i] = x + 1

        return n - lps[n-1]
