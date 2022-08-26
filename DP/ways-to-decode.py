class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        mod = 1000000007
        N = [0 for x in range(len(A))]
        A = [int(i) for i in A]
        if A[0] > 0:
            N[0] = 1
        for i in range(1, len(A)):
            if A[i] > 0:
                N[i] += N[i-1]
                N[i] %= mod
            if A[i-1]*10 + A[i] <= 26 and A[i-1]*10 + A[i] >= 10:
                if i == 1:
                    N[i] += 1
                    N[i] %= mod
                else:
                    N[i] += N[i-2]
                    N[i] %= mod
        return N[len(A)-1] % mod


print(Solution().numDecodings('5163490394499093221199401898020270545859326357520618953580237168826696965537789565062429676962877038781708385575876312877941367557410101383684194057405018861234394660905712238428675120866930196204792703765204322329401298924190'))
