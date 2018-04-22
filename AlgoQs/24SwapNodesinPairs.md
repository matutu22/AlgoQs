# 24. Swap Nodes in Pairs


Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.  

Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

---

##### Solution 1:

    class Solution(object):
        def swapPairs(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if not head:
                return
            if not head.next:
                return head
            next = head.next
            head.next = self.swapPairs(head.next.next)
            next.next = head
            return next
            
            
            
##### Solution 2:
	
    class Solution(object):
        def swapPairs(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """


            if not head:
                return
            l = ListNode(0)
            l.next = head
            dummy = l
            while dummy.next and dummy.next.next:
                first = dummy.next
                second = dummy.next.next
                first.next = second.next
                dummy.next = second
                dummy.next.next = first
                dummy = dummy.next.next
            return l.next