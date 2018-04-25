# 208. Implement Trie (Prefix Tree)



Implement a trie with insert, search, and startsWith methods.

Note:  
You may assume that all inputs are consist of lowercase letters a-z.



---

##### Solution 1:
	class TrieNode:
    
        def __init__(self):
            self.isWord = False

            # Can use a hashtable
            # Or use an array [26]
            self.tree = {}

	class Trie:

        def __init__(self):
            """
            Initialize your data structure here.
            """
            
            self.root = TrieNode()


        def insert(self, word):
            """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            """
            
            node = self.root
            for w in word:
                if w not in node.tree:
                    node.tree[w] = TrieNode()
                node = node.tree[w]
            node.isWord = True


        def search(self, word):
            """
            Returns if the word is in the trie.
            :type word: str
            :rtype: bool
            """
            
            node = self.root
            for w in word:
                if w not in node.tree:
                    return False
                else:
                    node = node.tree[w]
            return node.isWord


        def startsWith(self, prefix):
            """
            Returns if there is any word in the trie that starts with the given prefix.
            :type prefix: str
            :rtype: bool
            """
            
            node = self.root
            for p in prefix:
                if p not in node.tree:
                    return False
                else:
                    node = node.tree[p]
            return True


    # Your Trie object will be instantiated and called as such:
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)