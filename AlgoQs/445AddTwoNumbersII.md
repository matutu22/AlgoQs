# 445. Add Two Numbers II


You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:  


    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)  
    Output: 7 -> 8 -> 0 -> 7
---

##### Solution 1:

    class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """

            if not l1 or not l2:
                return
            stack1 = []
            stack2 = []
            while l1:
                stack1.append(l1.val)
                l1 = l1.next
            while l2:
                stack2.append(l2.val)
                l2 = l2.next

            def helper(num, node):
                temp = ListNode(num)
                temp.next = node
                node = temp
                return node

            add = 0
            node = None
            while stack1 and stack2:
                a = stack1.pop()
                b = stack2.pop()
                if a+b+add >=10:
                    c = (a+b+add)%10
                    add = 1

                else:
                    c = a + b + add
                    add = 0
                node = helper(c,node)

            while stack1:
                a = stack1.pop()

                if a+add >=10:
                    add = 1
                    c = (a+add)%10
                else:
                    c = a + add
                    add = 0
                node = helper(c,node)

            while stack2:
                b = stack2.pop()

                if b+add >=10:
                    add = 1
                    c = (b+add)%10
                else:
                    c = b + add
                    add = 0
                node = helper(c,node)

            if add == 1:
                node = helper(add,node)

            return node


                    
                