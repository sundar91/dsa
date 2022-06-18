# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        fast = slow = A
        flag = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break

        if flag == False:
            return A

        fast = A
        prev = None
        while fast != slow:
            prev = slow
            fast = fast.next
            slow = slow.next

        if prev:
            prev.next = None

        return A


f = ListNode(6)
s = ListNode(5)
f.next = s
t = ListNode(5)
s.next = t
fr = ListNode(3)
t.next = fr
fi = ListNode(8)
#fi.next = ListNode(6)
fr.next = fi

print(Solution().solve(f))
