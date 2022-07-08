# Given an integer A, you have to find the Ath Perfect Number.

# A Perfect Number has the following properties:

# It comprises only 1 and 2.

# The number of digits in a Perfect number is even.

# It is a palindrome number.

# For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.

from collections import deque


class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        s = ["" for i in range(0, 100005)]
        s[1] = "1"
        s[2] = "2"
        q = deque()
        q.append(s[1])
        q.append(s[2])
        idx = 3
        while idx < (A + 3):
            ss = q.popleft()
            s[idx] = ss + "1"
            idx = idx + 1
            q.append(ss + "1")
            s[idx] = ss + "2"
            idx = idx + 1
            q.append(ss + "2")
        ans = s[A]
        anss = ans
        # reverse
        ans = anss[::-1]
        return anss + ans
