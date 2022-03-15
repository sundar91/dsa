# Given an array B of length A with elements 1 or 0. Find the number of subarrays with bitwise OR 1.

class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        last = 0
        ans = 0
        for i in range(A):
            if B[i] == 1: last = i+1
            ans += last
        return ans



# Since the operation is a bitwise OR any subarray with atleast one element as 1 will have bitwise or 1.
# Well every subarray has a unique pair of left and right end indices. 
# Now for every index i in the array find in how many subarrays with bitwise OR 1, it is the right index of. 
# And add this value to ans.

# We can find this by seaching how many valid left index is present if current index i is taken as right index.
# If j is the first index that has B[j] = 1 to the left of i (including i), 
# then index 1 to j all can be taken as left index as there is atlest one 1 is the subarray. 
# so ans += j for that particular i