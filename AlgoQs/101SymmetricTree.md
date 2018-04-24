# 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3
But the following [1,2,2,null,3,null,3] is not:  

                1
               / \
              2   2
               \   \
               3    3


---


##### Solution :
	
    class Solution(object):
        def isSymmetric(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            def helper(left,right):
                if not left or not right:
                    return left == right
                if left.val != right.val:
                    return False
                return helper(left.left,right.right) and helper(left.right, right.left)
            if not root:
                return True
            return helper(root.left, root.right)