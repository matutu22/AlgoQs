# 415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
 
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.


---


##### Solution 1:
    class Solution(object):
        def addStrings(self, num1, num2):
            """
            :type num1: str
            :type num2: str
            :rtype: str
            """
            add = 0
            result = ""
            i=len(num1)-1
            j = len(num2)-1
            base = ord('0')
            while i >= 0 or j >= 0:
                n = 0
                if i >= 0:
                    n += ord(num1[i]) - base
                    i -= 1
                if j >= 0:
                    n += ord(num2[j]) - base
                    j -= 1

                n += add
                if n >= 10:
                    result += str(n%10)
                    add = n/10
                else:
                    result += str(n)
                    add = 0
            if add > 0 :
                result += str(add)
            return result[::-1]