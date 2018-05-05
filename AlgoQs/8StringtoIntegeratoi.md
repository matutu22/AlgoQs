# 8. String to Integer (atoi)


Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.  

Example 1:   

    Input: "42"  
    Output: 42  

Example 2:  

    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.
Example 3:

    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical 
                 digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                 Thefore INT_MIN (−231) is returned.

---


##### Solution 1:
    class Solution(object):
        def myAtoi(self, str):
            """
            :type str: str
            :rtype: int
            """
            if not str:
                return 0
            i = 0
            base = 0
            positive = 1
            m = 2**31
            l = len(str)

            # Skip Blank space
            while i < l and str[i] == " ":
                i += 1

            # Check positive or negative
            if i < l:
                if str[i] == "-":
                    positive = -positive
                    i += 1
                elif str[i] == "+":
                    i += 1


            # Check number, *10 each time
            # If it is larger then INTMAX/10, overflow
            while i < len(str):
                num = ord(str[i]) - ord("0")
                if num <0 or num > 9: 
                    break
                if base > m/10 or base==m/10 and num >= m%10:
                    return m-1 if positive == 1 else -m
                base = base*10 + num
                i += 1

            return base*positive
                

