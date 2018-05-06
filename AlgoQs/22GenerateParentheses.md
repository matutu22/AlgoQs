# 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]


---


##### Solution 1:
    class Solution(object):
        def generateParenthesis(self, n):
            """
            :type n: int
            :rtype: List[str]
            """
            result = []

            def helper(path, start, end, n, result,l):
                if l == 2*n:
                    result.append(path)

                if start < n:
                    helper(path+"(", start+1,end,n,result,l+1)

                if end < start:
                    helper(path+")", start,end+1,n,result,l+1)


            helper("", 0, 0, n, result, 0)

            return result