# 102. Binary Tree Level Order Traversal


Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],  

        3
       / \
      9  20
        /  \
       15   7
         
return its level order traversal as:  

        [
          [3],
          [9,20],
          [15,7]
        ]

---

##### Solution 1:
	class Solution(object):
        def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """

            if not root:
                return []

            stack = [root]
            result = []
            while stack:
                result.append([node.val for node in stack])
                temp = []
                for node in stack:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                stack = temp

            return result
            
            
            
##### Solution 2:
	    if not root:
            return []
        result = []
        queue = [(root,0)]
        
        while queue:
            node, level = queue.pop(0)
            if level >= len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
                
        return result

                
                    
        
                    
                