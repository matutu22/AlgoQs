# 106. Construct Binary Tree from Inorder and Postorder Traversal




Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]  
postorder = [9,15,7,20,3]  
Return the following binary tree:  


        3
       / \
      9  20
        /  \
       15   7
---

##### Solution:

	class Solution(object):
        def buildTree(self, inorder, postorder):
            """
            :type inorder: List[int]
            :type postorder: List[int]
            :rtype: TreeNode
            """
            if not postorder or not inorder:
                return

            val= postorder.pop()
            index = inorder.index(val)
            root = TreeNode(val)
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index],postorder)

            return root
