# 236. Lowest Common Ancestor of a Binary Tree




Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

          _______3______
         /              \
      ___5__          ___1__
     /      \        /      \
     6      _2       0       8
           /  \
           7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.  

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
            stack = [root]
            dic = {root:None}

            while q not in dic or p not in dic:
                node = stack.pop()
                if node.left:
                    dic[node.left] = node
                    stack.append(node.left)
                if node.right:
                    dic[node.right] = node
                    stack.append(node.right)

            a = set()

            while p in dic:
                a.add(p)
                p = dic[p]
            while q not in a:
                q = dic[q]

            return q

                   
                   
                   
                   
 ##### Solution 2 Recursively:
     class Solution(object):
        def lowestCommonAncestor(self, root, p, q):
            if not root or root == p or root == q:
                return root 

            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)

            if not left:
                return right
            elif not right:
                return left
            else:
                return root
