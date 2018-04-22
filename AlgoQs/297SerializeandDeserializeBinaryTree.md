# 297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

        1
       / \
      2   3
         / \
        4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


---

##### Solution:
	# Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Codec:

        def serialize(self, root):
            """Encodes a tree to a single string.

            :type root: TreeNode
            :rtype: str
            """

            # Iteratively
            queue = [root]
            result = []
            while queue:
                node = queue.pop()
                if node:
                    result.append(str(node.val))
                    queue.append(node.right)
                    queue.append(node.left)
                else:
                    result.append("null")
            return " ".join(result)

            # Recursively
    #         def helper(root):
    #             if root:
    #                 result.append(str(root.val))
    #                 helper(root.left)
    #                 helper(root.right)
    #             else:
    #                 result.append("null")
    #         result = []
    #         helper(root)
    #         return " ".join(result) 




        def deserialize(self, data):
            """Decodes your encoded data to tree.

            :type data: str
            :rtype: TreeNode
            """

            data = data.split()
            for i in range(len(data)):
                if data[i] == "null":
                    data[i] = None
                else:
                    data[i] = int(data[i])

            #return self.build(data)
            return self.buildTree(data, -1)[0]

        # Method 1
        def build(self, data):
            head = data.pop(0)
            if head == None:
                return None
            else:
                node = TreeNode(head)
                node.left = self.build(data)
                node.right = self.build(data)
            return node 


        # Method 2   
        def buildTree(self, data, pos):
            pos += 1
            if pos >= len(data) or data[pos]==None:
                return None, pos

            root = TreeNode(data[pos])
            root.left, pos = self.buildTree(data, pos)
            root.right, pos = self.buildTree(data, pos)
            return root, pos


    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))
