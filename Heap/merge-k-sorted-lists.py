# Definition for singly-linked list.
from __future__ import barry_as_FLUFL


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        h = []
        head = ListNode(None)
        for i in range(len(A)):
            h.append(A[i])
            self.buildMinHeap(h, len(h) - 1)

        current = head
        n = len(h)
        while current:
            current.next = h[0]
            if h[0] is None:
                break
            h[0] = h[0].next
            if h[0] is None:
                h[0] = h[n-1]
                h[n-1] = None
                n = n - 1

            self.heapify(h, n, 0)
            current = current.next

        return head.next

    def buildMinHeap(self, A, index):
        while index > 0:
            pi = (index-1) // 2

            if A[pi].val > A[index].val:
                A[pi], A[index] = A[index], A[pi]
                index = pi
            else:
                break

    def heapify(self, A, n, index):
        while index < n:
            left = 2 * index + 1
            right = 2 * index + 2

            smallest = index
            if left < n and A[left].val < A[smallest].val:
                smallest = left

            if right < n and A[right].val < A[smallest].val:
                smallest = right

            if smallest == index:
                break

            A[smallest], A[index] = A[index], A[smallest]
            index = smallest


a = ListNode(3)
b = ListNode(10)
b.next = ListNode(20)
a.next = b

i = ListNode(4)
j = ListNode(11)
j.next = ListNode(13)
i.next = j

x = ListNode(1)
y = ListNode(8)
y.next = ListNode(9)
x.next = y

print(Solution().mergeKLists([a, i, x]))
