# You are given a string A of lowercase English alphabets. Rearrange the characters of the given string A such that there is no boring substring in A.

# A boring substring has the following properties:

# 1. Its length is 2.
# 2. Both the characters are consecutive, for example - "ab", "cd", "dc", "zy" etc.(If the first character is C then the next character can be either (C+1) or (C-1)).
#
# Return 1 if it is possible to rearrange the letters of A such that there are no boring substrings in A else, return 0.

def check(a, b):
    c = a + b
    for i in range(1, len(c)):
        res = ord(c[i]) - ord(c[i - 1])
        if res < 0:
            res = (-1) * res
        if res == 1:
            return 0
    return 1


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        odd = ""
        even = ""
        for a in A:
            if ord(a) % 2:
                odd += a
            else:
                even += a
        o = sorted(odd)
        e = sorted(even)
        if check(o, e):
            return 1
        elif check(e, o):
            return 1
        else:
            return 0

# another solution


def solve(A):
    count = [0] * 26
    n = len(A)

    for i in range(n):
        indx = ord(A[i]) - ord('a')
        count[indx] += 1

    for i in range(25):
        # distributing consecutive characters is greater than half of length + 1 then we cannot remove boring string
        if (count[i] + count[i+1]) > (n+1) / 2:
            return 0

    return 1
