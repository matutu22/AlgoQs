# 206. Reverse Linked List


Reverse a singly linked list.

---

##### Solution 1 Recursively:
  Time complexity: O(n)  
  Space complexity: O(1)
    
        def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
            def helper(head,temp):
                if not head:
                    return temp
                next = head.next
                head.next = temp
                return helper(next,head)

            return helper(head,None)
        
##### Solution 2 Iteratively:

        def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
         
            temp = None
            while head:
                next = head.next
                head.next = temp
                temp = head
                head = next
            return temp

