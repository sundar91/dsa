class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        s = self.expandBrackets(A)
        s1 = self.expandBrackets(B)

        print(s)
        print(s1)

        for i in range(26):
            if s[i] != s1[i]:
                return 0
        return 1

    def expandBrackets(self, A):

        MAX_CHARS = 26
        v = [0] * MAX_CHARS
        stck = []
        stck.append(True)

        i = 0
        while i < len(A):

            if A[i] == '+' or A[i] == '-':
                i += 1
                continue

            if A[i] == '(':
                if self.checkSign(A, i):
                    stck.append(stck[-1])
                else:
                    stck.append(not stck[-1])

            elif A[i] == ')':
                stck.pop()

            else:
                if stck[-1]:
                    v[ord(A[i]) - ord('a')] = 1 if self.checkSign(A, i) else -1
                else:
                    v[ord(A[i]) - ord('a')] = -1 if self.checkSign(A, i) else 1

            i += 1

        return v

    def checkSign(self, A, i):
        if i == 0:
            return True
        elif A[i-1] == '-':
            return False

        return True


sol = Solution()
print(sol.solve("-(a+b+c)", "-a+b-c"))
