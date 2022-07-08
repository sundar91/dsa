class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        s = []
        res = []
        prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

        for i in range(len(A)):
            val = A[i]

            # remove higher priority from stack and put new operator in stack
            if val in prec:
                if len(s) == 0:
                    s.append(val)
                else:
                    top = s[-1]
                    while top in prec and prec[val] <= prec[top]:
                        res.append(s.pop())
                        if len(s) == 0:
                            break
                        top = s[-1]
                    s.append(val)

            elif val == ')':
                top = s[-1]
                s.pop()
                while top != '(':
                    res.append(top)
                    top = s[-1]
                    s.pop()

            elif val == '(':
                s.append(val)
            else:
                res.append(val)
        while len(s) > 0:
            res.append(s.pop())

        return ''.join(res)

# xbt+/g*ho-s^*ez-/
# xbt+/g*ho-^s*ez-/
# xbt+/g*ho-s^*ez-/
print(Solution().solve("x/(b+t)*g*(h-o)^s/(e-z)"))
