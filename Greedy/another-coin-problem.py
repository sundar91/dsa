class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        num = A
        ans = 0
        while num > 0:
            ans += num % 5
            num = num // 5

        return ans


print(Solution().solve(443))
