import sys
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# sys.setrecursionlimit(1000000000)


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        temp = A

        if A is None or A.next is None:
            return A

        mid = self.findMiddle(temp)
        h2 = mid.next
        mid.next = None

        h2 = self.sortList(h2)
        h1 = self.sortList(temp)

        t = self.merge(h1, h2)

        return t

    def findMiddle(self, A):
        fast = slow = A
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def merge(self, A, B):
        dummy = ListNode(-1)
        t = dummy
        h1, h2 = A, B

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


f = ListNode(4)
s = ListNode(2)
f.next = s
t = ListNode(1)
s.next = t
fr = ListNode(5)
t.next = fr
fi = ListNode(3)
fr.next = fi


print(Solution().sortList(f))
