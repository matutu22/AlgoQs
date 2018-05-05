# 23. Merge k Sorted Lists


Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:  

    [
      1->4->5,
      1->3->4,
      2->6
    ]
Output: 1->1->2->3->4->4->5->6

---


##### Solution 1:
Divide the input list and merge each two lists.

	class Solution(object):
        def mergeKLists(self, lists):
            """
            :type lists: List[ListNode]
            :rtype: ListNode
            """

            def mergeTwoLists(l1, l2):

                result = ListNode(0)
                l = result
                while l1 and l2:

                    if l1.val < l2.val:
                        l.next = ListNode(l1.val)
                        l1 = l1.next

                    else:
                        l.next = ListNode(l2.val)

                        l2 = l2.next
                    l=l.next
                if l1:
                    l.next = l1
                elif l2:
                    l.next = l2
                return result.next

            if not lists:
                return

            l = len(lists)
            if l == 1:
                return lists[0]

            mid = l/2
            right = self.mergeKLists(lists[mid:])
            left = self.mergeKLists(lists[:mid])

            return mergeTwoLists(left,right)
            
            
            
            
##### Solution 2:

Use a priority Queue to store the unmerged list


        if not lists:
            return
        
        import Queue
        q = Queue.PriorityQueue()
        for list in lists:
            if list:
                q.put((list.val, list))

        dummy = ListNode(0)
        l = dummy
        
        while not q.empty():
            val, node = q.get()
            l.next = node
            l = l.next
            if node.next:
                q.put((node.next.val, node.next))
            
        return dummy.next

