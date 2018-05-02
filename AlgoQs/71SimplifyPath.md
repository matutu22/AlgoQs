# 71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,  
path = "/home/", => "/home"  
path = "/a/./b/../../c/", => "/c"

click to show corner cases.

Corner Cases:  


 

 

    Did you consider the case where path = "/../"?  
    In this case, you should return "/".  
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".  
    In this case, you should ignore redundant slashes and return "/home/foo".



---

##### Solution 1:
	class Solution(object):
        def simplifyPath(self, path):
            """
            :type path: str
            :rtype: str
            """
            path = path.split("/")
            stack = []
            for p in path:
                if p == "..":
                    if stack:
                        stack.pop()
                elif p != "" and p !=".":
                    stack.append(p)
            return "/" + "/".join(stack)