# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def detectCycle(self, A):
        fast = slow = A
        flag = False
        # move fast pointer with velocity = 2 and for slow  velocity = 1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break

        if flag == False:
            return None

        fast = A
        # move both pointer with velocity = 1
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast


# Solution Approach :

# Lets now look at the starting point.
# If we were using hashing, the first repetition we get is the starting point. Simple!

# What happens with the 2 pointer approach ?

# Method 1 :
# If you detect a cycle, the meeting point is definitely a point within the cycle.

# Can you determine the size of the cycle ? ( Easy ) Let the size be k.
# Fix one pointer on the head, and another pointer to kth node from head.
# Now move them simulataneously one step at a time. They will meet at the starting point of the cycle.


# Method 2 :
# This might be slightly more complicated. It involves a bit of maths and is not as intuitive as method 1.
# Suppose the first meet at step k,the distance between the start node of list and the start node of cycle is s, and the distance between the start node of cycle and the first meeting node is m.
# Then
# df = m + xn + k  
# ds = m + yn + k where n is an integer denotes length of nodes in a cycle.
# df = 2ds
# m + xn + k = 2(m + yn + k)
# m + k = n (x - 2y)

# So, if we have one pointer on the head and another pointer at the meeting point. Note that since the distance between start node of cycle and the first meeting node is m, 
# therefore if the pointer moves (m + k) steps, it will reach the start of the cycle. When the pointer at the head moves s steps, 
# the second pointer moves  steps which both points to the start of the cycle. In other words, both pointers meet first at the start of the cycle.
