# Given a linked list A, remove the B-th node from the end of the list and return its head.

# For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.

# NOTE: If B is greater than the size of the list, remove the first node of the list.

# NOTE: Try doing it using constant additional space.


# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if not A:
            return A
        tail = A
        for _ in range(B):
            tail = tail if tail is None else tail.next
        if tail is None:
            return A.next
        prev = None
        curr = A
        while tail:
            tail = tail.next
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return A