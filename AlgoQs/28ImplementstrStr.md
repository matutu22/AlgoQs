# 28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"  
Output: 2  

Example 2:

Input: haystack = "aaaaa", needle = "bba"  
Output: -1  

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


##### Solution :
	class Solution(object):
        def strStr(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """
            if not needle:
                return 0

            length = len(haystack)
            len1 = len(needle)

            if len1>length:
                return -1
            for index in range(length-len1+1):
                temp = index
                for j in range(len1):
                    if needle[j] != haystack[temp]:
                        break
                    else:
                        if j == len1 -1:
                            return index
                        temp += 1
                index += 1
            return -1
                
                    
        
                    
                