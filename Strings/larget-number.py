# Given an array A of non-negative integers, 
# arrange them such that they form the largest number.

# Note: The result may be very large, so you need to 
# return a string instead of an integer.

# Examples:
#  A = [3, 30, 34, 5, 9]
#  Explanation 1:

# Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.


from fractions import Fraction
import functools
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, key=lambda n: Fraction(n, 10 ** len(str(n)) - 1), reverse = True)
        i = 0
        while i < len(A) - 1:
            if A[i] != 0:
                break
            else:
                i += 1
        ret = map(lambda x:str(x), A[i:])
        return ''.join(ret)



class Solution2:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        l = sorted(A, key = functools.cmp_to_key(self.compare))
        return int(''.join([str(i) for i in l]))


    def compare(self, a, b):
        if str(a) + str(b) > str(b) + str(a):
            return -1
        if str(a) + str(b) < str(b) + str(a):
            return 1
        return 0