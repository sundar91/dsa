# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseKElement(self, A, k):

        current = A
        reversedList = current
        for _ in range(k - 1):
            reversedList = reversedList.next

        prev = None
        while current:
            count = 1
            last = current
            while last.next is not None and count < k:
                last = last.next
                count += 1

            nxt = last.next
            last.next = None
            p = self.reverse(current)
            if prev is not None:
                prev.next = p

            prev = current
            current = nxt

        return reversedList

    def reverse(self, current):
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev


f = ListNode(1)
s = ListNode(2)
f.next = s
t = ListNode(3)
s.next = t
fr = ListNode(4)
t.next = fr
fi = ListNode(5)
fi.next = ListNode(6)
fr.next = fi

print(Solution().reverseKElement(f, 2))
