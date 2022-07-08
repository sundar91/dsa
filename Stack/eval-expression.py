# Input 1:
#     A =   ["2", "1", "+", "3", "*"]

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        ret = 0
        first = 0
        second = 0
        for a in A:
            if a == '+' or a == '-' or a == '/' or a == '*':
                if len(stack) < 2:
                    return 0
                second = stack.pop()
                first = stack.pop()
                if a == '+':
                    ret = first + second
                    stack.append(ret)
                elif a == '-':
                    ret = first - second
                    stack.append(ret)
                elif a == '*':
                    ret = first * second
                    stack.append(ret)
                elif a == '/':
                    ret = first // second
                    stack.append(ret)
            else:
                stack.append(int(a))
        if len(stack) == 1:
            return stack[0]
        else:
            return 0
