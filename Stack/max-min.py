class Solution:

    def smallerLeft(self, A):

        n = len(A)
        ans = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                ans[stack[-1]] = i
                stack.pop(-1)
            stack.append(i)
        return ans

    def smallerRight(self, A):
        n = len(A)
        ans = [n] * n
        stack = []
        for i in range(0, n):
            while stack and A[stack[-1]] >= A[i]:
                ans[stack[-1]] = i
                stack.pop(-1)
            stack.append(i)
        return ans

    def greaterLeft(self, A):
        n = len(A)
        ans = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] < A[i]:
                ans[stack[-1]] = i
                stack.pop(-1)
            stack.append(i)
        return ans

    def greaterRight(self, A):

        n = len(A)
        ans = [n] * n
        stack = []
        for i in range(0, n):
            while stack and A[stack[-1]] <= A[i]:
                ans[stack[-1]] = i
                stack.pop(-1)
            stack.append(i)
        return ans

    # Contribution Technique
    # For each element, consider in how many subarrays => it is maximum element
    # Similarly, consider in how many subarrays => it is minimum element

    def solve(self, A):

        m = pow(10, 9) + 7
        s = 0
        n = len(A)
        if n == 1:
            return 0

        nsr = self.smallerRight(A)
        nsl = self.smallerLeft(A)
        ngr = self.greaterRight(A)
        ngl = self.greaterLeft(A)

        for i in range(n):
            # A[i] acts as a maximum in subarrays range from ngr to ngl
            s += ((ngr[i] - i) * (i - ngl[i]) * A[i])

            # A[i] acts as a minimum subarrays range from nsr to nsl
            s -= ((nsr[i] - i) * (i - nsl[i]) * A[i])
            s = s % m
        return s


print(Solution().solve([4, 7, 3, 8]))
