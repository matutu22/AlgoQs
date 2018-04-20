# 186. Reverse Words in a String II


Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array

Update (2017-10-16):
We have updated the function signature to accept a character array, so please reset to the default code definition by clicking on the reload button above the code editor. Also, Run Code is now available!

---

##### Solution:

+ First reverse each word
+ Then add last word reversed
+ Then reverse whole string



  
    class Solution:
        def reverseWords(self, str):
            """
            :type str: List[str]
            :rtype: void Do not return anything, modify str in-place instead.
            """
            def helper(string, start, end):
                while start < end:
                    string[start], string[end] = string[end], string[start]
                    start += 1
                    end -= 1

            i = 0

            for index, char in enumerate(str):
                if char == " ":
                    helper(str,i,index-1)
                    i = index + 1
            helper(str, i, len(str)-1)
            helper(str, 0, len(str)-1)