# 173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.




---

##### Solution 1:

	
    class BSTIterator(object):
        def __init__(self, root):
            """
            :type root: TreeNode
            """
            self.stack = []
            while root:
                self.stack.append(root)
                root = root.left


        def hasNext(self):
            """
            :rtype: bool
            """
            if not self.stack:
                return False
            else:
                return True


        # If call next() n times
        # Append n nodes at right 
        # Therefore average O(1)
        def next(self):
            """
            :rtype: int
            """
            if not self.hasNext():
                return 
            node = self.stack.pop()
            right = node.right

            while right:
                self.stack.append(right)
                right = right.left
            return node.val



    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next())