# Given a singly linked list A

#  A: A0 → A1 → … → An-1 → An
# reorder it to:

#  A0 → An → A1 → An-1 → A2 → An-2 → …
# You must do this in-place without altering the nodes' values.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        h1 = A
        mid = self.findMiddle(h1)

        h2 = mid.next
        mid.next = None

        h2 = self.reverse(h2)

        dummy = ListNode(-1)
        t = dummy
        count = 1
        while h1 and h2:
            if count % 2 != 0:
                t.next = h1
                h1 = h1.next
                t = t.next
            else:
                t.next = h2
                h2 = h2.next
                t = t.next
            count += 1

        if h1:
            t.next = h1
        else:
            t.next = h2

        return dummy.next

    def reverse(self, A):
        temp = A
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        return prev

    def findMiddle(self, A):
        fast = slow = A
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow
