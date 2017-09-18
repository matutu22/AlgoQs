class Solution(object):
    def convertToBase7(self, num, base):
        """
        :type num: int
        :rtype: str
        """
        output = ""
        if not num:
            return "0"
        negative = False
        if num<0:
            negative = True
            num = -num
        while num:
            a = num % base
            output = str(a) +output
            num = num/base
        if negative==True:
            return str(-int(output))
        else: 
            return output
