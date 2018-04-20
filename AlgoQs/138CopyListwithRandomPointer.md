# 138. Copy List with Random Pointer

##### A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

##### Return a deep copy of the list.

---

##### Solution 1:
  Time complexity: O(n)  
  Space complexity: O(1)

        def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        
        # Copy each node once, double list
        temp = head
        while temp:
            next = temp.next
            temp.next = RandomListNode(temp.label)
            temp = temp.next
            temp.next = next
            temp = temp.next
        
        # Assign copied nodes' random pointer
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        # Restore original list, and get copied list
        newhead = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return newhead
        
 ##### Solution 2:
   Time Complexity: O(n)  
   Space: O(n)
   
        def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        
        # Copy each node once, double list
        temp = head
        while temp:
            next = temp.next
            temp.next = RandomListNode(temp.label)
            temp = temp.next
            temp.next = next
            temp = temp.next
        
        # Assign copied nodes' random pointer
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        # Restore original list, and get copied list
        newhead = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return newhead