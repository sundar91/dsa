class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        carry  = 0
        current =  res
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            s = carry + x + y
           
            carry = int(s / 10)
            s =  s % 10
            
            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next
                
            current.next = ListNode(s)
            current = current.next
            
        if carry > 0:
            current.next = ListNode(carry)
        
        return res.next


l1 = ListNode(2, ListNode(4, ListNode(3)))

l2 = ListNode(5, ListNode(6, ListNode(4)))
print(Solution().addTwoNumbers(l1, l2))