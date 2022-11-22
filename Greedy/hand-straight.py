# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.


# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

from collections import defaultdict
import heapq


class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minh = list(count.keys())
        heapq.heapify(minh)

        print(minh)

        while minh:
            i = minh[0]
            for n in range(i, i + groupSize):
                if n not in count:
                    return False

                count[n] -= 1
                if count[n] == 0:
                    if n != minh[0]:
                        return False
                    heapq.heappop(minh)

        return True


# print(Solution().isNStraightHand([1, 1, 3, 6, 2, 3, 4, 7, 8], 3))
