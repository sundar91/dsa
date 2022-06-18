# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        current = A
        head = current
        count = 0
        prev = None
        while current:
            count += 1
            if count == B:
                p = self.reverseList(current, B, C)
                if prev is None:
                    prev = p
                    head = p
                else:
                    prev.next = p
                break
            else:
                prev = current
                current = current.next

        return head

    def reverseList(self, current, B, C):
        p = None
        count = 0
        k = C - B + 1
        temp = current
        while current and count < k:
            count += 1
            nxt = current.next
            current.next = p
            p = current
            current = nxt

        temp.next = nxt
        return p


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

print(Solution().reverseBetween(f, 2, 4))
