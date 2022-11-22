# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.


# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9, 7, 8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.


class Solution:
    def partitionLabels(self, s: str):

        h = {}
        output = []
        # storing last index of each character
        for i in range(len(s)):
            h[s[i]] = i

        size, end = 0, 0
        for i in range(len(s)):
            size += 1
            end = max(end, h[s[i]])
            if i == end:
                output.append(size)
                size = 0

        return output


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
