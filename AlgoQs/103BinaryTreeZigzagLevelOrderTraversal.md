# 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],  

        3
       / \
      9  20
        /  \
       15   7
return its zigzag level order traversal as:  

    [
      [3],
      [20,9],
      [15,7]
    ]

---

##### Solution 1:
	
    class Solution(object):
        def zigzagLevelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if not root:
                return []
            result = []
            stack = [(root,0)]
            while stack:
                node, level = stack.pop()
                if level >= len(result):
                    result.append([])
                if level % 2 == 1:
                    result[level] = [node.val] + result[level]
                else:
                    result[level].append(node.val)
                if node.right:
                    stack.append((node.right,level+1))
                if node.left:
                    stack.append((node.left,level+1))
            return result



                    
                