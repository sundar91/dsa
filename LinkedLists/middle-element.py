# Given a linked list of integers, find and return the middle element of the linked list.

# NOTE: If there are N nodes in the linked list and N is even then return the (N/2 - 1)th element.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):

        if A is None or not A.next:
            return A

        # slow = fast = A
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        # return slow.val

        fast = slow = A
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow.val


f = ListNode(1)
s = ListNode(2)
f.next = s
t = ListNode(3)
s.next = t
fr = ListNode(4)
t.next = fr
fi = ListNode(5)
# fr.next = fi


print(Solution().solve(f))
