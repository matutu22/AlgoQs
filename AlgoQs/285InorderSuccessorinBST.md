# 285. Inorder Successor in BST


Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.




---

##### Solution 1 Iteratively:


    class Solution(object):
        def inorderSuccessor(self, root, p):
            """
            :type root: TreeNode
            :type p: TreeNode
            :rtype: TreeNode
            """

            pre = None
            while root:
                if p.val >= root.val:
                    root = root.right
                else:
                    pre= root
                    root = root.left

            return pre
            
            
##### Solution 2 Recursively:
	    if not root:
            return 
            
        # If p.val >= root.val then successor must in the right    
        if p.val >= root.val:
            return self.inorderSuccessor(root.right,p)
        else:
            if not self.inorderSuccessor(root.left,p):
                return root
            else:
                return self.inorderSuccessor(root.left,p)
                    
