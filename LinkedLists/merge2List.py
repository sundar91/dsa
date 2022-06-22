# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        dummy = ListNode(-1)
        t = dummy
        h1 = A
        h2 = B
        while h1 and h2:
            if h1.val <= h2.val:
                t.next = h1
                h1 = h1.next
                t = t.next
            else:
                t.next = h2
                h2 = h2.next
                t = t.next

        if h1:
            t.next = h1
        else:
            t.next = h2

        return dummy.next
