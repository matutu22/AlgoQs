class Solution(object):


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
            
        # Reusable func
        def tonextcount(l):
            next = ""
            i = 0
            count = 1
            if len(l) == 1:
                return "1" + str(l)
            
            while i < len(l)-1:
                if l[i] == l[i+1]:
                    count += 1
                    i+= 1
                    continue
                else:
                    next += (str(count)+str(l[i]))
                    count =1
                i += 1
            if count!= 1:
                next += (str(count)+str(l[-1]))
            if l[-1] != l[-2]:
                next += "1" + str(l[-1])
            return next
                
        list = []
        for index in range(0,n):
            list.append("")
        list[0] = "1"
        index = 1
        while index < n:
            list[index] = tonextcount(list[index-1])
            index += 1
        return list[n-1]
