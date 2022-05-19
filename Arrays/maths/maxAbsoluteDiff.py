# You are given an array of N integers, A1, A2, …. AN.

# Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# |A[i] - A[j]| + |i - j|
# since f(i,j) = f(j,i) so we can look for i < j
# |A[i] - A[j]| + j - i
# case 1: A[i] <= A[j]
# A[j] - A[i] + j - i = A[j] + j - A[i] - i = (A[j] + j) - (A[i] + i)
# difference is max if first part is max and second part min
# case 2: A[i] > A[j]
# A[i] - A[j] + j -i = (A[i] - i) - (A[j] - j)
# max of both cases


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        Xmax, Xmin, Ymax, Ymin = float(
            '-Inf'), float('Inf'), float('-Inf'), float('Inf')
        for i in range(len(A)):
            Xmax = max(Xmax, A[i] - i)
            Xmin = min(Xmin, A[i] - i)
            Ymax = max(Ymax, A[i] + i)
            Ymin = min(Ymin, A[i] + i)

        return max(Xmax - Xmin, Ymax - Ymin)
