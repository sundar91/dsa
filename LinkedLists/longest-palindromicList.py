# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):

        current = A
        resLen = 0

        prev = None
        # odd sequence and reverse
        while current:
            left, right = prev, current.next
            count = 1

            while left and right and left.val == right.val:
                left = left.next
                right = right.next
                count += 2

            if count > resLen:
                resLen = count

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        head = prev
        prev = None
        current = head
        # even sequence
        while current and current.next:

            right = current.next
            # if next value is equal then we only proceed for current as center
            if current.val == right.val:
                count = 2
                left, right = prev, right.next

                while left and right and left.val == right.val:
                    left = left.next
                    right = right.next
                    count += 2

                if count > resLen:
                    resLen = count

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return resLen


f = ListNode(2)
s = ListNode(3)
f.next = s
t = ListNode(3)
s.next = t
fr = ListNode(3)
t.next = fr
fi = ListNode(1)
# fi.next = ListNode(6)
#fr.next = fi

print(Solution().solve(f))
