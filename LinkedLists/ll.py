from turtle import pos


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def insert(self, position, value):

        if position == 1:
            self.insertAtStart(value)
            return

        if position > self.length + 1:
            position = self.length

        node = self.findKNode(position - 1)
        newnode = ListNode(value)
        nxt = node.next
        node.next = newnode
        newnode.next = nxt

        self.length += 1

    def insertAtStart(self, value):
        node = ListNode(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def delete_node(self, position):
        if position > self.length:
            return

        if position == 1:
            self.head = self.head.next
            self.length -= 1
            return

        node = self.findKNode(position - 1)
        node.next = node.next.next
        self.length -= 1

    def findKNode(self, position):
        temp = self.head
        count = 1
        while count < position and temp:
            temp = temp.next
            count += 1
        return temp

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

        print('')


ll = LinkedList()

ll.insert(1, 22)

ll.insert(2, 23)

ll.insert(4, 24)
ll.print_ll()
ll.delete_node(2)

ll.print_ll()
