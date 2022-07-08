
# merge sort
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        if n <= 1:
            return A

        s1 = []
        for _ in range((n//2)):
            s1.append(A[0])
            A.pop(0)

        s2 = self.solve(A)
        s1 = self.solve(s1)
        return self.merge(s1, s2)

    def merge(self, s1, s2):
        s = []
        while s1 and s2:
            if s1[-1] >= s2[-1]:
                s.append(s1[-1])
                s1.pop()
            else:
                s.append(s2[-1])
                s2.pop()

        while s1:
            s.append(s1[-1])
            s1.pop()
        while s2:
            s.append(s2[-1])
            s2.pop()

        return s[::-1]


print(Solution().solve([66, 96, 43, 28, 14, 1, 41, 76,
      70, 81, 22, 11, 42, 78, 4, 88, 70, 43, 90, 6, 12]))


# another solution -> pop every element from tmpstck and put back to original stack until we find the current smallest


class Solution2:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        tmpstack = []
        while(len(A) != 0):
            tmp = A.pop()
            while(len(tmpstack) != 0):
                val = tmpstack.pop()
                if(val > tmp):
                    A.append(val)
                else:
                    tmpstack.append(val)
                    break
            tmpstack.append(tmp)
        return tmpstack
