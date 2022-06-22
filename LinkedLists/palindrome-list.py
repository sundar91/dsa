# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        left = None
        fast = slow = A
        right = A

        # go uptil middle (reverse until middle)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            nxt = right.next
            right.next = left
            left = right
            right = nxt

        # if it is odd so move right pointer
        if fast:
            right = right.next

        #compare left and right part
        while right:
            if right.val != left.val:
                return 0

            left = left.next
            right = right.next

        return 1


f = ListNode(1)
s = ListNode(1)
f.next = s
t = ListNode(6)
s.next = t
fr = ListNode(4)
t.next = fr
fi = ListNode(1)
# fi.next = ListNode(6)
fr.next = fi

print(Solution().lPalin(f))
