# 171. Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28   
    
---

##### Solution:
	class Solution(object):
        def titleToNumber(self, s):
            """
            :type s: str
            :rtype: int
            """
            result = 0

            for char in s:
                result = result * 26 + ord(char) - 64
            return result 
