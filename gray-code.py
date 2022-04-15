class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans = []
        for i in range(2 ** A):
            ans.append((i>>1) ^ i)
        return ans


## Recursive Approach

# class Solution:
#     # @param A : integer
#     # @return a list of integers
#     def grayCode(self, A):
#         if A <= 0:
#             return [0]
#         if A == 1:
#             return [0, 1]
        
#         gen_codes = self.grayCode(A-1)
#         res = list(gen_codes)
       
#         for i in range(len(gen_codes) -1 , -1, -1):
#             b = '{:0{}b}'.format(gen_codes[i], A-1)
#             res.append(int('1' + b, 2))
        
#         return res