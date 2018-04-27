# 146. LRU Cache



Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4



---

##### Solution:
Use a dictionary with key is the key, value is the Node,  
USe a double linked list, with head is the most recently element  
Double linked list  can delete a node without iterate



    class Node:

        def __init__(self,k,v):
            self.key = k
            self.value = v
            self.next = None
            self.pre = None

    class LRUCache(object):

        def __init__(self, capacity):
            """
            :type capacity: int
            """
            self.capacity = capacity
            self.dic = {}
            self.head= Node(0,0)
            self.tail = Node(0,0)
            self.count = 0
            self.head.next = self.tail
            self.tail.pre = self.head

        def get(self, key):
            """
            :type key: int
            :rtype: int
            """
            if key in self.dic:
                cur = self.dic[key]
                self.moveToHead(cur)
                return cur.value

            return -1


        def put(self, key, value):
            """
            :type key: int
            :type value: int
            :rtype: void
            """
            if key in self.dic:
                node = self.dic[key]
                node.value = value
                self.moveToHead(node)
            else:
                if self.count >= self.capacity:
                    last = self.tail.pre
                    self.dic.pop(last.key,None)
                    self.removeNode(last)
                    cur = Node(key,value)
                    self.dic[key] = cur
                    self.addNode(cur)
                else:
                    node = Node(key,value)
                    self.dic[key] = node
                    self.addNode(node)
                    self.count += 1


        def removeNode(self, node):
            pre = node.pre
            next = node.next

            pre.next = next
            next.pre = pre

        def addNode(self, node):
            node.pre = self.head
            node.next= self.head.next

            self.head.next.pre= node
            self.head.next = node



        def moveToHead(self, node):
            self.removeNode(node)
            self.addNode(node)


    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)