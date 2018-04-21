# 235. Lowest Common Ancestor of a Binary Search Tree




Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

          _______6______
         /              \
      ___2__          ___8__
     /      \        /      \
     0      _4       7       9
           /  \
           3   5
           
             
             
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

---

##### Solution 1 Iteratively:
	class Solution(object):
        def lowestCommonAncestor(self, root, p, q):
            """
            :type root: TreeNode
            :type p: TreeNode
            :type q: TreeNode
            :rtype: TreeNode
            """
            # Iterative
            a, b = q.val, p.val
            while root:
                c = root.val
                if a < c and b < c:
                    root = root.left
                elif a > c and b > c:
                    root = root.right
                else:
                    return root
                   
                   
                   
                   
 ##### Solution 2 Recursively:
		class Solution(object):
            def lowestCommonAncestor(self, root, p, q):
                """
                :type root: TreeNode
                :type p: TreeNode
                :type q: TreeNode
                :rtype: TreeNode
                """
                # Recursive
                a, b = q.val, p.val
                if root.val > a and root.val > b:
                    return self.lowestCommonAncestor(root.left, p, q)
                elif root.val < a and root.val < b:
                    return self.lowestCommonAncestor(root.right, p, q)
                else:
                    return root
