# 112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

---

##### Solution :
	
    class Solution(object):
        def hasPathSum(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: bool
            """
            if not root:
                return False
            stack = [(root,root.val)]
            while stack:
                node,s = stack.pop()
                if s == sum and not node.left and not node.right:
                    return True
                if node.left:
                    stack.append((node.left, s+node.left.val))
                if node.right:
                    stack.append((node.right, s+node.right.val))
            return False