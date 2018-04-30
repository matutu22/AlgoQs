# 114. Flatten Binary Tree to Linked List


Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

        1
       / \
      2   5
     / \   \
    3   4   6
The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

---

##### Solution:
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution(object):
        def flatten(self, root):
            """
            :type root: TreeNode
            :rtype: void Do not return anything, modify root in-place instead.
            """
            if not root:
                return
            dummy = root
            while dummy:
                if dummy.left:
                    pre = dummy.left
                    while pre.right:
                        pre = pre.right
                    pre.right = dummy.right
                    dummy.right = dummy.left
                    dummy.left= None

                dummy = dummy.right

