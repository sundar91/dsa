class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stck = []
        i = 0
        while i < len(A):

            s = ''
            while A[i] != "/" :
                s += A[i]
                i += 1

            if s == '.' or s == '':
                i += 1
                continue

            if s == '..':
                if len(stck) > 0:
                    stck.pop()
                i += 1
                continue

            stck.append(s)
            i += 1

        s = ""
        for i in range(len(stck)):
            s += "/" + stck[i]

        return s


# print(Solution().simplifyPath("/a/./b/../../c/"))
print(Solution().simplifyPath("/.."))
