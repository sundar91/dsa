from functools import cache
from typing import OrderedDict
import collections


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.hm = {}
        self.head = None
        self.tail = None

    # @return an integer

    def get(self, key):
        if key not in self.hm:
            return -1

        node = self.hm[key]
        self.removenode(node)
        self.insertattail(node.key, node.value)

        return self.hm[key].value

    # @param key, an integer
    # @param value, an integer
    # @return nothing

    def set(self, key, value):
        # if key is already in cache place that it at last
        if key in self.hm:
            node = self.hm[key]
            self.removenode(node)
            self.insertattail(key, value)
            return

        # if key is not there and capacity is still not full then insert at tail
        if len(self.hm) < self.capacity:
            self.insertattail(key, value)
            return

        # remove head and insert a new node at tail
        self.removenode(self.head)
        self.insertattail(key, value)

    def removenode(self, node):
        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            node.prev.next = node.next

        # if it is tail
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        del self.hm[node.key]

    def insertathead(self, key, value):
        if self.head is not None:
            return

        node = ListNode(key, value)
        self.head = node
        self.tail = self.head

        self.hm[key] = node

    def insertattail(self, key, value):
        if self.head is None:
            self.insertathead(key, value)
            return

        node = ListNode(key, value)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        self.hm[key] = node


c = LRUCache(7)
c.set(2, 1)
c.set(1, 10)
c.set(8, 13)
print(c.get(12))
c.set(2, 8)
print(c.get(11))
print(c.get(7))
c.set(14, 7)
c.set(12, 9)
c.set(7, 10)
print(c.get(11))
c.set(9, 3)
c.set(14, 15)
print(c.get(15))
print(c.get(9))
c.set(4, 13)
print(c.get(3))
c.set(13, 7)
print(c.get(2))
c.set(5, 9)
print(c.get(6))
print(c.get(13))
c.set(4, 5)
c.set(3, 2)
c.set(4, 12)
print(c.get(13))
print(c.get(7))
c.set(9, 7)
print(c.get(3))
print(c.get(6))
print(c.get(7))


# using ordered dict simple approach

class LRUCache2:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)

        self.cache[key] = value
