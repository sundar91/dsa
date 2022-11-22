# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

from array import array


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                # there are three option add '(',  add ')' and empty string
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0


# print(Solution().checkValidString("())"))
# print(Solution().checkValidString("(*))"))


arr = array("i", [2, 1, 3, 4, 7, 6, 4, 6, 9])

print(4 in arr)
for i in range(len(arr)+1):
    if arr[i] in arr[i+1:]:
        break
