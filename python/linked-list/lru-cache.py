# Design a data structure that follows the constraints 
# of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with 
# positive size capacity.
# int get(int key) Return the value of the key if the key exists, 
# otherwise return -1.
# void put(int key, int value) Update the value of the key if the 
# key exists. Otherwise, add the key-value pair to the cache. 
# If the number of keys exceeds the capacity from this operation, 
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # capacity constant, map to link keys to node to get value, references to first and last node
        self.map = {}
        self.capacity = capacity
        self.cur_size = 0
        self.prehead = Node(-1, -1)
        self.posttail = Node(-2, -1)
        self.prehead.next = self.posttail
        self.posttail.prev = self.prehead

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(key)
            self.add(node.key, node.val)
        
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
            self.add(key, value)
        else:
            if self.cur_size == self.capacity:
                self.remove(self.prehead.next.key)
            self.add(key, value)

    def remove(self, key):
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.cur_size -= 1
        del self.map[key]
        
    def add(self, key, value):
        node = Node(key, value)
        self.map[key] = node
        self.cur_size += 1
        self.posttail.prev.next = node
        node.prev = self.posttail.prev
        node.next = self.posttail
        self.posttail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)