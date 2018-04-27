# 204. Count Primes



Description:

Count the number of prime numbers less than a non-negative number, n.



---

##### Solution :
    class Solution(object):
        def countPrimes(self, n):
            """
            :type n: int
            :rtype: int
            """
            boolPrime = [False] * n
            for i in xrange(2,int(n**0.5)+1):
                if not boolPrime[i]:
                    j = i*i
                    while j<n:
                        boolPrime[j] = True
                        j+= i

            return boolPrime[2:].count(False) 