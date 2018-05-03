# 92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:  

    Input: 1->2->3->4->5->NULL, m = 2, n = 4  
    Output: 1->4->3->2->5->NULL

---

##### Solution 1:
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution(object):
        def reverseBetween(self, head, m, n):
            """
            :type head: ListNode
            :type m: int
            :type n: int
            :rtype: ListNode
            """
            if not head:
                return 
                
            dummy = ListNode(0)
            dummy.next = head
            l = dummy
            
            for _ in range(m-1):
                l=l.next
                
            start = l.next

            # l is the node before reversed, ONE in this case
            # start is the start node to be reversed
            # Always move start.next to l.next, to the head
            # In the second step, attach strat.next.next to start.next (Delete start.next)
            # In the third step, attach l.next(l.next is the start without the node to be reversed) to next.next
            # Finally, update l.next with next.
            # The head of next always remain unchanged
            for i in range(n-m):
                next = start.next
                start.next = next.next
                next.next = l.next
                l.next = next
            return dummy.next


