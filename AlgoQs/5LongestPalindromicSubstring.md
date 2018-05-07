# 5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"
Note: "aba" is also a valid answer.  

Example 2:

    Input: "cbbd"
    Output: "bb"


---


##### Solution 1:
    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            def helper(s,i,j):
                while i >= 0 and j < l and s[i] == s[j]:
                    i -= 1
                    j += 1
                return s[i+1:j]

            l = len(s)
            if l ==0:
                return ""

            result = ""
            for i in range(l):
                r = helper(s,i,i)
                if len(r) > len(result):
                    result = r

                r = helper(s,i,i+1)
                if len(r) > len(result):
                    result = r

            return result
